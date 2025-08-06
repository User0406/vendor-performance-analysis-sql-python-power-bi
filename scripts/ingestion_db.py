logging.basicConfig(
    filename='logs/ingestion_db.log',
    level = logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filemode = 'a'
)


engine  = create_engine('sqlite:///inventory.db')

def ingest_db(df,table_name,engine):
    df.to_sql(table_name, con = engine, if_exists = 'replace', index = False)
    
def load_raw_data():    ## this fucnt will load the csv as df and ingest into db
    start = time.time()
    for file in os.listdir('data'):
        df = pd.read_csv('data/'+file)
        logging.info(f'ingestion {file} in db')
        ingest_db(df, file[:-4], engine)
        
    end = time.time()
    total_time = (end - start)/60
    logging.info('----------ingestion complete--------------')
    
    logging.info(f'total time taken: {total_time} minute')

if __name__=='__main__':
    load_raw_data()