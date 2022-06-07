# Data Vectorization / Word Embedding
        
        It is a process of converting text data to numerical vectors.

# Objective of code:
    This code converts textual data into numerical vectors and stores the numerical data into database.

## Libraries Used
#### 1. transformers:
                    1.a AutoTokenizer: It is used to reduce a sentence to tokens (words) and then encode the token to 
                                       numerical vectors.It returns a dictionary with 3 items:
                                                    i) input_ids are the indices corresponding to each token in the sentence.
                                                    ii) attention_mask indicates whether a token should be attended to or not.
                                                    iii) token_type_ids identifies which sequence a token belongs to when there is more than one sequence.

#### 2. sqlite3: 
                    A library used to create and manage database and tables. 


## Database Structure

### Database name:  vectorized.db
Contains 1 table with 1 column:
                                         
                                        vectors   

                               |        vector   | 
                               |-----------------|
                               |        TEXT     |        
                               | (contains list) |   

## User defined functions:
1. create_table: Create a table named **vectors**.
2. delete_table: Delete the table.
3. create_vectors: returns input_ids of the vectorized tokens created by tokenizer object of AutoTokenizer class in numeric form.
4. decode_vectors: decodes the numeric input_ids stored in database table and return the original string.
5. insert: To insert multiple items into database using executemany.
6. fetch: To fetch all the data from database.


## Working of Code
This code takes the batch of strings as inputs and convert them into vectorised numeric form, then store the input id's 
of the vector into **_vectors_** table in database named **_vectorized.db_** 
Then it fetches and print all the items from the **_vectors_** table and decode them back to their original string.
This code uses "bert-base-cased" pretrained model from pre_trained class of AutoTokenizer to create tokens 
and perform word embedding.