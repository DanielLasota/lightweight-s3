from lightweight_s3 import S3Client, StorageConnectionParameters


if __name__ == '__main__ ':

    storage_connection_parameters = StorageConnectionParameters(
        backblaze_access_key_id='access_key_id',
        backblaze_secret_access_key='secret_access_key',
        backblaze_endpoint_url='endpoint_url',
        backblaze_bucket_name='bucket_name'
    )

    """
    Or just put em into the .env file. Load the .env using:
    
            load_dotenv(env_path)
    
    and then read it using:
    
            storage_connection_parameters = StorageConnectionParameters()
    """

    s3_client = S3Client(storage_connection_parameters)

    s3_client.upload_existing_file(file_path='C:/JohnnySins/Documents/SomeFile.csv')

    s3_client.upload_zipped_jsoned_string(
        data='some_sophisticated_data....',
        file_name='some_csv_name.csv'
    )

    s3_client.shutdown()
