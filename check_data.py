import pandas as pd

# Load the generated TSV file
df = pd.read_csv('abr_filtered_output.tsv', sep='\t', encoding='utf-8-sig')

print('=' * 50)
print('📊 DATA VALIDATION REPORT')
print('=' * 50)

# 1. Total row count
print(f'Total extracted records: {len(df):,}')

# 2. Check for missing values (NaN) across key columns
print('\n🔍 Missing values check (empty cells):')
print(df.isnull().sum())

# 3. Distribution by entity type (Entity_Type)
# Key checkpoint to verify business logic filtering
print('\n🏢 Entity type distribution:')
if 'Entity_Type' in df.columns:
  print(df['Entity_Type'].value_counts())
else:
  print("[WARNING] Column 'Entity_Type' not found!")

# 4. Display first 3 rows for visual inspection
print('\n👀 First 3 rows of the dataset:')
print(df.head(3))
print('=' * 50)
