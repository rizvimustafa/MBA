Each algorithm has been implemented in a separate file
[Apriori.py, PCY.py, SON.py, RandomSampling.py, PCYmultihash.py]


 INSTRUCTIONS ON HOW TO RUN EACH FILE:

Apriori.py
    Before running the algorithm:
        In __name__ == "__main__":
            Set file_name = Specify the file you want to process by providing its name and location. If
            the file is located within the project folder, you can simply provide the file name,
            like "retail.txt." If the file is not within the folder, please
            enter the complete file path, such as "C:\Users\musta\Downloads\retail.data."
            Set min_support = The minimum support threshold.
                              [For eg. 0.01 for 1% support,
                                       0.02 for 2% support,
                                       0.1 for 10% support,
                                       0.5 for 50% support]

    You're all prepared to execute Apriori.py! Upon running Apriori.py, the console will display
    the execution time. The Frequent Item Pairs from your file will be saved in a text file
    located within your project folder. This text file will be named as follows:
    "freq-itemsets_apriori_support" + min_support_percentage +"%" + file_name + ".txt"
    For eg. "freq-itemsets_apriori_support1.0%retail.data.txt". Here min_support = 0.01 so
    min_support_percentage = 1.0%, and file_name = retail.data

    The txt file will contain frequent item pairs separated by a comma.
    For eg.
    (38, 41)
    (39, 225)
    (39, 170)
    (39, 48)
    ......

PCY.py

    Before running the algorithm:
        In __name__ == "__main__":
            Set file_name = Specify the file you want to process by providing its name and location. If
            the file is located within the project folder, you can simply provide the file name,
            like "retail.txt." If the file is not within the folder, please
            enter the complete file path, such as "C:\Users\musta\Downloads\retail.data."
            Set min_support = The minimum support threshold.
                              [For eg. 0.01 for 1% support,
                                       0.02 for 2% support,
                                       0.1 for 10% support,
                                       0.5 for 50% support]
            Set hash_bucket_size =
                              For retail.data and similar sized datasets set it to 997
                              For netflix.data and similar sized datasets set it to 9997

    You're all prepared to execute PCY.py! Upon running PCY.py, the console will display
    the execution time. The Frequent Item Pairs from your file will be saved in a text file
    located within your project folder. This text file will be named as follows:
    "freq-itemsets_pcy_support" + min_support_percentage +"%" + file_name + ".txt"
    For eg. "freq-itemsets_pcy_support1.0%retail.data.txt". Here min_support = 0.01 so
    min_support_percentage = 1.0%, and file_name = retail.data

    The txt file will contain frequent item pairs separated by a comma.
    For eg.
    (38, 41)
    (39, 225)
    (39, 170)
    (39, 41)
    ......


SON.py (Uses PCY Algorithm)

    Before running the algorithm:
        In __name__ == "__main__":
            Set file_name = Specify the file you want to process by providing its name and location. If
            the file is located within the project folder, you can simply provide the file name,
            like "retail.txt." If the file is not within the folder, please
            enter the complete file path, such as "C:\Users\musta\Downloads\retail.data."
            Set min_support = The minimum support threshold.
                              [For eg. 0.01 for 1% support,
                                       0.02 for 2% support,
                                       0.1 for 10% support,
                                       0.5 for 50% support]
            Set hash_bucket_size =
                              For retail.data and similar sized datasets set it to 997
                              For netflix.data and similar sized datasets set it to 9997

            Set chunk_size =
                              For retail.data and similar sized datasets set it to 50000
                              For netflix.data and similar sized datasets set it to 8000

    You're all prepared to execute SON.py! Upon running SON.py, the console will display
    the execution time. The Frequent Item Pairs from your file will be saved in a text file
    located within your project folder. This text file will be named as follows:
    "freq-itemsets_son_support" + min_support_percentage +"%" + file_name + ".txt"
    For eg. "freq-itemsets_son_support1.0%retail.data.txt". Here min_support = 0.01 so
    min_support_percentage = 1.0%, and file_name = retail.data

    The txt file will contain frequent item pairs separated by a comma.
    For eg.
    (38, 41)
    (39, 225)
    (39, 170)
    (39, 41)
    ......


RandomSampling.PY (Uses PCY Algorithm)

    Before running the algorithm:
        In __name__ == "__main__":
            Set file_name = Specify the file you want to process by providing its name and location. If
            the file is located within the project folder, you can simply provide the file name,
            like "retail.txt." If the file is not within the folder, please
            enter the complete file path, such as "C:\Users\musta\Downloads\retail.data."
            Set min_support = The minimum support threshold.
                              [For eg. 0.01 for 1% support,
                                       0.02 for 2% support,
                                       0.1 for 10% support,
                                       0.5 for 50% support]
            Set hash_bucket_size =
                              For retail.data and similar sized datasets set it to 997
                              For netflix.data and similar sized datasets set it to 9997

            Set sample_size =
                              For retail.data and similar sized datasets set it to 10000
                              For netflix.data and similar sized datasets set it to 50000

    You're all prepared to execute RandomSampling.py! Upon running RandomSampling.py, the console will display
    the execution time. The Frequent Item Pairs from your file will be saved in a text file
    located within your project folder. This text file will be named as follows:
    "freq-itemsets_sampling_support" + min_support_percentage +"%" + file_name + ".txt"
    For eg. "freq-itemsets_sampling_support1.0%retail.data.txt". Here min_support = 0.01 so
    min_support_percentage = 1.0%, and file_name = retail.data

    The txt file will contain frequent item pairs separated by a comma.
    For eg.
    (38, 41)
    (39, 225)
    (39, 170)
    (39, 41)
    ......



PCYmultihash.PY

    Before running the algorithm:
        In __name__ == "__main__":
            Set file_name = Specify the file you want to process by providing its name and location. If
            the file is located within the project folder, you can simply provide the file name,
            like "retail.txt." If the file is not within the folder, please
            enter the complete file path, such as "C:\Users\musta\Downloads\retail.data."
            Set min_support = The minimum support threshold.
                              [For eg. 0.01 for 1% support,
                                       0.02 for 2% support,
                                       0.1 for 10% support,
                                       0.5 for 50% support]
            Set hash_bucket_size =
                              For retail.data and similar sized datasets set it to 499
                              For netflix.data and similar sized datasets set it to 4999

            Set num_hash_tables =
                              For retail.data and similar sized datasets set it to 3
                              For netflix.data and similar sized datasets set it to 4

    You're all prepared to execute PCYmultihash.py! Upon running PCYmultihash.py, the console will display
    the execution time. The Frequent Item Pairs from your file will be saved in a text file
    located within your project folder. This text file will be named as follows:
    "freq-itemsets_pcymultihash_support" + min_support_percentage +"%" + file_name + ".txt"
    For eg. "freq-itemsets_pcymultihash_support1.0%retail.data.txt". Here min_support = 0.01 so
    min_support_percentage = 1.0%, and file_name = retail.data

    The txt file will contain frequent item pairs separated by a comma.
    For eg.
    (38, 41)
    (39, 225)
    (39, 170)
    (39, 41)
    ......
