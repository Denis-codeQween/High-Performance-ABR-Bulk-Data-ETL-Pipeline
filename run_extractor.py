import os
import time
import csv
from lxml import etree

DATA_DIR = "." 
OUTPUT_REPORT = "abr_filtered_output.tsv"

# Целевые коды типов организаций из требований задачи
TARGET_CODES = {"PUB", "OIE"}

def process_xml_stream(file_path):
    file_name = os.path.basename(file_path)
    print(f"[INFO] Parsing and filtering: {file_name}")
    record_count = 0
    matched_count = 0
    extracted_data = []

    try:
        context = etree.iterparse(file_path, events=('end',), tag='ABR')
        
        for event, elem in context:
            record_count += 1
            
            record_date = elem.get('recordLastUpdatedDate', 'N/A')
            
            abn_elem = elem.find('ABN')
            abn_value = abn_elem.text if (abn_elem is not None and abn_elem.text) else 'N/A'
            status_value = abn_elem.get('status', 'N/A') if abn_elem is not None else 'N/A'
            
            name_elem = elem.find('.//NonIndividualName/NonIndividualNameText')
            org_name = name_elem.text if (name_elem is not None and name_elem.text) else 'N/A'

            # Ищем код типа организации
            entity_type_code = 'N/A'
            for subelem in elem.iter():
                if subelem.tag and 'entity' in subelem.tag.lower() and subelem.text:
                    entity_type_code = subelem.text.strip()
                    break

            # СТРОГАЯ ФИЛЬТРАЦИЯ: сохраняем только PUB и OIE
            if entity_type_code in TARGET_CODES:
                extracted_data.append([
                    abn_value.strip(),
                    org_name.strip(),
                    entity_type_code,
                    status_value,
                    record_date,
                    file_name
                ])
                matched_count += 1

            elem.clear()
            while elem.getprevious() is not None:
                del elem.getparent()[0]

            if record_count % 100000 == 0:
                print(f"  [DEBUG] [{file_name}] Processed: {record_count:,} | Matched: {matched_count:,}")

    except Exception as e:
        print(f"[ERROR] Failed processing {file_name}: {e}")

    print(f"[SUCCESS] Finished {file_name}. Total processed: {record_count:,}, Filtered & Matched: {matched_count:,}\n")
    return extracted_data

def main():
    start_time = time.time()
    print("=" * 65)
    print("🚀 ABR DATA FILTERING & ETL PIPELINE")
    print("=" * 65)

    all_records = []
    xml_files = sorted([f for f in os.listdir(DATA_DIR) if f.endswith('.xml')])
    
    if not xml_files:
        print("[WARNING] No XML files found!")
        return

    for xml_file in xml_files[:1]:
        file_path = os.path.join(DATA_DIR, xml_file)
        data = process_xml_stream(file_path)
        all_records.extend(data)

    if all_records:
        print(f"[INFO] Exporting clean filtered TSV file to: {OUTPUT_REPORT}")
        
        with open(OUTPUT_REPORT, mode='w', newline='', encoding='utf-8-sig') as f:
            writer = csv.writer(f, delimiter='\t')
            writer.writerow(['ABN', 'Organization_Name', 'Entity_Type', 'Status', 'Updated_Date', 'Source_File'])
            writer.writerows(all_records)
            
        print(f"[SUCCESS] Export complete. Total filtered rows in spreadsheet: {len(all_records):,}")

    elapsed_time = time.time() - start_time
    print("=" * 65)
    print(f"✨ Finished in {elapsed_time:.2f} seconds.")
    print("=" * 65)

if __name__ == "__main__":
    main()