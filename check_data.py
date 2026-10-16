import pandas as pd

# Загружаем полученный TSV-файл
df = pd.read_csv('abr_filtered_output.tsv', sep='\t', encoding='utf-8-sig')

print("=" * 50)
print("📊 ОТЧЕТ ПО ПРОВЕРКЕ ДАННЫХ")
print("=" * 50)

# 1. Общее количество строк
print(f"Всего извлечено записей: {len(df):,}")

# 2. Проверка на пустые значения (NaN) по ключевым полям
print("\n🔍 Проверка на пропущенные значения (пустые ячейки):")
print(df.isnull().sum())

# 3. Распределение по типам организаций (Entity_Type)
# Это ключевой пункт для проверки бизнес-логики задания
print("\n🏢 Распределение по типам организаций:")
if 'Entity_Type' in df.columns:
    print(df['Entity_Type'].value_counts())
else:
    print("[ПРЕДУПРЕЖДЕНИЕ] Колонка 'Entity_Type' не найдена!")

# 4. Вывод первых 3 строк для визуальной оценки
print("\n👀 Первые 3 строки датасета:")
print(df.head(3))
print("=" * 50)