# Walrus
*Not just a Movie Recommendation System*

Walrus is Movie analysis and recommendation service that runs on IBM's Natural Language Understanding.
It splits the dataset in order to run 3 primary tasks *Emotion Analyzer,Concept Analyzer,Character Similarity from Wikipedia*

## Tools and API's used
1.IBM Watson Natural Language Understanding Service - Analyze text to extract concepts, keywords, emotion using natural language understanding.

2.Google Pre-trained word2vec model – Find closeness between words to establish similarity between entities.

3.MediaWiki API – Extract contents from Wikipedia page to perform analysis.

4.Kivy Cross Platform Application Development – Create desktop application.

## Functional Modules
### Emotion Analyzer
Using the Natural Language Understanding(NLU) API, analyzes the trend of 5 emotions across every scene of the movie, and finds other movies that have similar patterns of emotion changes. 

### Concept Analyzer
From the plot of each movie, the basic concepts are obtained using the IBM Watson NLU API Service. With the help of Google word2vec model, it finds other movies that have similar concepts and plots. 

### Artist Analyzer
Using the MediaWiki API provided by Wikipedia to access data, the primary artists of the movie, the actors and directors are taken and the module finds other movies that have the same artists who have worked in it. The artist analyzer gives a more recognizable touch to recommendation of movies(insert better)

### Character Similarity
Once the movies are recommended, to provide a personal touch and how the movie may be similar to the original movie, the characters from the recommended movie are matched with characters of the previous movie based on similarity index, which is calculated using the word vector file provided in the dataset.


### Major Issues
This project primarily focused on developing both mathematical and functional models of analysing a movie dataset. Hence, a major component in any project UI/UX was overlooked. The UI developed for this application is built on kivy and is standalone desktop application. Future improvements to be made include acquistion and processing of a larger dataset and developing an aesthetic User Interface. 
