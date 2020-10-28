import app.loader as loader
import app.writer as writer

def run():
    records = loader.import_records()
    for key, records in records.items():
        writer.write(key, records)

if __name__ == '__main__':
    run()




