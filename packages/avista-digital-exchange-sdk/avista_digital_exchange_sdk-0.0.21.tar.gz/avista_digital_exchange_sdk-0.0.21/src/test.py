import avista_digital_exchange_sdk_

instance = avista_digital_exchange_sdk_.AvistaDigitalExchange(
    "e5502e44-5779-40a0-acaf-b2b40e155f72988bb717-be38-4dab-9ecf-67651c997761", True)

result = instance.getUserInfo()
print(result)
result = instance.listDataStores()
#result = instance.getDataStore('dataStore.d996a5ab-09c2-4c17-ab69-35ce439fdb47')
#result = instance.getDataStoreDirectory('dataStoreDirectory.f4d73518-5b94-4a1a-a61d-2ed303966d52')
#result = instance.downloadDataStoreFile('dataStoreFile.ccc27535-afcb-420d-a46c-18dd44a73d8c', './')

#result = instance.listCollaboratives()
#result = instance.getCollaborative('collaborative.a9c96586-6ebe-457f-ba22-25c55237fde5')
#result = instance.listCollaborativeServices('collaborative.03f2cabb-c20e-4c93-a6b3-c42dfeeb7d58')
#result = instance.listCollaborativesServiceSharedWith('dataStore.d996a5ab-09c2-4c17-ab69-35ce439fdb47')

#result = instance.listTimeSeriesDatabases()
#result = instance.getTimeSeriesDatabase('timeSeriesDb.d6260509-dc3f-4c32-9f8d-aa8a437d080e')

#result = instance.queryTimeSeriesDatabaseWithTimestreamFormat('timeSeriesDb.85478fa6-c99b-4a9a-9c99-d6f2872c38fc', 'SELECT * FROM "avista-digital-exchange-host-org-db"."timeSeriesDb.85478fa6-c99b-4a9a-9c99-d6f2872c38fc" WHERE time between ago(300d) and now() ORDER BY time DESC ', 500)

#result = instance.uploadFileToDataStore('dataStore.1e22ac26-c623-4209-a1d3-340dd25f6f5b', 'dataStoreDirectory.f4d73518-5b94-4a1a-a61d-2ed303966d52', 'localFile.txt')
#result = instance.deleteDataStoreFile('dataStoreFile.abe277b9-4238-4626-828e-8c4e0f73090b')
#result = instance.addServiceToCollaborative('dataStore.1e22ac26-c623-4209-a1d3-340dd25f6f5b', 'collaborative.a5849776-2da9-4183-8522-f4dacfe0b1dd')
