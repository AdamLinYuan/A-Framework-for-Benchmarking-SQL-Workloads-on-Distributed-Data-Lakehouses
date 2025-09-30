#!/usr/bin/env python3
"""
Simple TPC-H Test for Week 1 - Fixed and Working Version
"""

import trino

def main():
    print("🚀 TPC-H Week 1 Test - Clean Setup")
    print("=" * 50)
    
    # Connect to Trino
    conn = trino.dbapi.connect(
        host="localhost", 
        port=8080, 
        user="adam"
    )
    cur = conn.cursor()
    
    # Test 1: Basic connection
    cur.execute("SELECT 1")
    print(f"✅ Connection: {cur.fetchone()[0]}")
    
    # Test 2: Available catalogs
    cur.execute("SHOW CATALOGS")
    catalogs = [c[0] for c in cur.fetchall()]
    print(f"📁 Catalogs: {', '.join(catalogs)}")
    
    # Test 3: TPC-H schemas
    cur.execute("SHOW SCHEMAS FROM tpch")
    schemas = [s[0] for s in cur.fetchall()]
    print(f"📊 TPC-H Scales: {', '.join(schemas)}")
    
    # Test 4: Row counts for SF1 (1GB)
    print(f"\n📈 TPC-H SF1 (1GB Dataset) Overview:")
    cur.execute("SHOW TABLES FROM tpch.sf1")
    tables = cur.fetchall()
    
    total_rows = 0
    for table in tables:
        table_name = table[0]
        cur.execute(f"SELECT COUNT(*) FROM tpch.sf1.{table_name}")
        count = cur.fetchone()[0]
        total_rows += count
        print(f"  - {table_name}: {count:,} rows")
    
    print(f"\n📊 Total rows: {total_rows:,}")
    print(f"💾 Dataset size: ~1GB")
    
    # Test 5: Simple analytical query
    print(f"\n🔍 Sample Query - Top 5 Nations by Name:")
    cur.execute("""
        SELECT name, nationkey, regionkey
        FROM tpch.sf1.nation 
        ORDER BY name 
        LIMIT 5
    """)
    
    for row in cur.fetchall():
        print(f"  - {row[0]} (ID: {row[1]}, Region: {row[2]})")
    
    # Test 6: Complex join query
    print(f"\n🚀 Complex Query - Customer Orders Summary:")
    cur.execute("""
        SELECT 
            COUNT(DISTINCT c.custkey) as total_customers,
            COUNT(o.orderkey) as total_orders,
            AVG(o.totalprice) as avg_order_value
        FROM tpch.sf1.customer c
        JOIN tpch.sf1.orders o ON c.custkey = o.custkey
        LIMIT 1
    """)
    
    result = cur.fetchone()
    print(f"  - Customers: {result[0]:,}")
    print(f"  - Orders: {result[1]:,}")
    print(f"  - Avg Order: ${result[2]:.2f}")
    
    print(f"\n✅ Week 1 Setup Complete!")
    print(f"🎯 Ready for benchmarking framework development")
    print("=" * 50)

if __name__ == "__main__":
    main()
