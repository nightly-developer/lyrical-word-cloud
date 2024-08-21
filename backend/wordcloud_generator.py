from wordcloud import WordCloud
import matplotlib.pyplot as plt

# Sample text
text = """
    I wanna run away
    Don't wanna lie, I don't want a life
    Send me a gun and I'll see the sun
    I'd rather run away
    You need an instant ease
    From your life where you got plenty
    Of every hurt and heartbreak
    You just take it all to the face
    I know that you want to cry
    But there's much more to life than dyin'
    Over your past mistakes
    And people who threw dirt on your name
"""

# Generate the word cloud
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)

# Display the word cloud using matplotlib
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')  # Turn off axis labels
plt.show()
