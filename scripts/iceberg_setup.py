import trino

def setup_iceberg_lakehouse():
    """Create Iceberg tables from TPC-H data for Week 1 goals"""
    
    conn = trino.dbapi.connect(
        host="localhost", 
        port=8080, 
        user="adam"
    )
    cur = conn.cursor()
    
    print("🧊 Setting up Iceberg Lakehouse with TPC-H data...")
    
    # Create schema
    cur.execute("CREATE SCHEMA IF NOT EXISTS iceberg.tpch_week1")
    print("✅ Created schema: iceberg.tpch_week1")
    
    # Tables to migrate (start with smaller ones for Week 1)
    tables = ['nation', 'region', 'supplier', 'customer']
    
    for table in tables:
        print(f"📦 Creating Iceberg table: {table}")
        
        try:
            # Check if table exists
            cur.execute(f"DROP TABLE IF EXISTS iceberg.tpch_week1.{table}")
            
            # Create Iceberg table with TPC-H data
            cur.execute(f"""
                CREATE TABLE iceberg.tpch_week1.{table}
                AS SELECT * FROM tpch.sf1.{table}
            """)
            
            # Verify row count
            cur.execute(f"SELECT COUNT(*) FROM iceberg.tpch_week1.{table}")
            count = cur.fetchone()[0]
            print(f"  ✅ {table}: {count:,} rows migrated to Iceberg")
            
        except Exception as e:
            print(f"  ❌ Error with {table}: {e}")
    
    print("\n🎯 Week 1 Iceberg setup complete!")
    print("📋 Next steps: Test schema evolution and time travel features")

if __name__ == "__main__":
    setup_iceberg_lakehouse()