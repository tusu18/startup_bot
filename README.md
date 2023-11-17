# Mentor Mentee Recommendation Bot

https://festive-noether-dfb657.netlify.app/
This Repository contains the trained model and the deployed file of the startup bot used in our Portal
>The Bot has been trained on more tahn 800 stories and can perform upto 10 actions
>Actions
  -Stock price
  -Find Mentor
  -Signup
  -Latest Startup news
  -Finding Incubators closest
  -Navigation


E. Machine Learning:
1. Mentor Recommendation: The model used for 
the mentor recommendation, which is one of the 
objectives of the portal has been developed using 
a standard approach of recommendation and the 
new method of using neural networks, then these 
two combined together to calculate the final 
score. So, the main thought or insight is to take 
both the linearity and non-linearity in 
consideration to make a robust recommendation.
i. Multilayer Perceptron Network (MLP): 
This can be simplified as the 
layers of neural network follow up by 
the nonlinear activation functions such 
as ReLu. The skeleton of our network 
is that it is made up of DN (Deep 
Network) of 4 feed forward layers these 
all are implemented using TensorFlow
which uses high level Keras API.
Rather than the traditional matrix dot 
products, this gives more insights into 
the data.
ii. Matrix Factorization Network (GMF):
This method includes our longlasting approach of dot products of the 
embedding (Matrix Factorization). 
Although a curated selection of 
hyperparameters would result in a 
faster recommendation. The method 
which we used, takes the benefits of 
both the worlds, i.e. the neural network 
and matrix factorization to act in 
robustness. The draw backs of MLP are 
overcome by the GMF.
The ‘clicks’ of the users, the blog 
reading time, their input as ratings to 
mentors and the blogs, would form as 
the source of our data to the network.
iii. Combining the two networks 
(NeuMF):
The recommendation engine 
combines the power of both, i.e. the 
multi-layer perceptron and the matrix 
factorization in the given order as 
below. The embeddings are flattened
and then it is fed to the network 
followed up by the single network.
Further, the setup consists of Adam 
optimizer with a binary cross entropy 
loss.
Fig 6. Combination of both the models.
2. Chatbot and Blog Summarization:
The field of NLP (Natural Language 
Processing) has seen a lot of developments 
recently with release of papers on BERT, T5, 
GPT. NLP has got a variety of applications in 
every field- be it text analysis, document 
retrieval, chat bots etc. The models have been 
developed on huge unstructured text data which 
makes the model flexible for various operations 
such as regression, classification, 
summarization, language generation, etc. A 
special mention to the paper “Exploring the 
Limits of Transfer Learning with a Unified Textto-Text Transformer” by Google team, enabled
us tune our model on a specific task as per our 
requirement. Due to availability of large text 
corpus such as C4 we have achieved state of the
art results thus setting aside benchmarks.
The NLP task can be classified on the basis 
of processes:
i. Tokenization.
ii. Intent Classification.
iii. Entities detection.
iv. Policies (Online Learning).
For the process of tokenization, we have 
used Whitespace Tokenizer. Currently our model is 
giving 97.36 on test stories in intent classification 
and 80.65 in entity extraction. We have used the 
DIET () classifier as it’s based on our specific 
domain. As we don’t have a large set of data, we 
have used the balance batching strategy.
Policies are used in order: First the 
Transformer embedded dialog policy and then the 
Memoization policy to detect previously learned 
stories of happy path and/ or sad path.
The T5 model is based on several tasks 
such that it can be fine-tuned on every minute detail. 
A single model (fine-tuned) trained on a corpus of 
data available on our portal, forms a solid interactive 
system as the model gives us the power to 
summarize, classify the blog tags used in the chat 
bot. We have used a simple transformer library by 
Hugging Face. It is basically a transformer model, 
which is tuned on a dataset scraped from Quora, ET, 
India Startup, etc. Tasks such as Regression, Q&A, 
Multi-label Classification can be performed. The 
output of the model would be displayed to the user 
using the interface of the portal.
However, this model could be further 
developed with the use of reformer model (since the 
transformer model is pre-trained on a huge amount 
of data) which is known as efficient transformer, 
which in turn would help our system to be quicker 
and more adaptable. It can also be made better by 
taking more efforts in gathering clean, realistic 
datasets
