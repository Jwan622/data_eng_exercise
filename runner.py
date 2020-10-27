import app.loader as loader
import app.writer as writer

def run():
    records = loader.import_records()
    for key, records in records.items():
        print(key)
        print(len(records))
        writer.write(key, records)

if __name__ == '__main__':
    run()




