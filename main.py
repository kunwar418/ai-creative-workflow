import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from src.bulk_processor import BulkProcessor
import time

def main():
    print("="*60)
    print("AI PRODUCT CREATIVE GENERATION WORKFLOW")
    print("="*60)
    
    while True:
        print("\n1. Process single URL")
        print("2. Process CSV file")
        print("3. Exit")
        choice = input("\nChoose option: ")
        
        if choice == '1':
            url = input("Enter product URL: ")
            processor = BulkProcessor()
            result = processor.process_single_url(url, f"job_{int(time.time())}")
            print("\n" + "="*60)
            print("RESULTS")
            print("="*60)
            if result:
                print(f"\nProduct: {result['product']}")
                print(f"\nGenerated {len(result['images'])} images:")
                for img in result['images']:
                    print(f"  - {img}")
                print(f"\nGenerated {len(result['videos'])} videos:")
                for vid in result['videos']:
                    print(f"  - {vid}")
            else:
                print("Processing failed")
        
        elif choice == '2':
            csv_path = input("Enter CSV file path (must have 'url' column): ")
            if not os.path.exists(csv_path):
                print("File not found. Creating sample CSV...")
                with open(csv_path, 'w') as f:
                    f.write("url\nhttps://example.com/product1\nhttps://example.com/product2")
            processor = BulkProcessor()
            results = processor.process_csv(csv_path)
            print(f"\nProcessed {len(results)} products")
            for r in results:
                if r:
                    print(f"  - {r['product']}: {len(r['images'])} images, {len(r['videos'])} videos")
        
        elif choice == '3':
            print("Thank you!")
            break

if __name__ == "__main__":
    main()