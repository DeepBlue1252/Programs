#!/usr/bin/env python
# coding: utf-8

# In[11]:


###########################################################################################################
# START OF IMPORTS AND SETTINGS
###########################################################################################################

# import libraries needed for this program
import csv
import numpy as np, pandas as pd, matplotlib.pyplot as plt
from scipy.stats import linregress

# adjust display settings for DataFrame to show more rows and columns from it
pd.set_option('display.max_rows', 10)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

###########################################################################################################
# END OF IMPORTS AND SETTINGS
###########################################################################################################


###########################################################################################################
# START OF MENU OPTIONS 1 THRU. 8
###########################################################################################################  

# function name: overview
# arguments: none
# return: none
# description: outputs an overview of your topic and data set
def overview():
    print('\n####################################################################################################################')
    print('\t\t\t\t\tAnime\n')
    print('The dataset provides the amount of episodes each series has. I would like to see if there is a comparison between the duration of the series and the rating? ')
    print('')
    print('The useful columns of this dataset are uid, title, genre, aired, episodes, members, popularity, ranked, and score')
    print('\n####################################################################################################################\n')
    
#dq
def dq():
    print('\n')
    print("Question 1: My first data driven question is, Is their a connection between the duration of a series and its rating?")
    print('\n')
    print("I think the rating of an anime will be higher the more episodes it has. From my experience, when an anime has more episodes, its easier to get attached.")
    print('\n')
    
#Basic Stats
def basic_stats():
    choice = ''
    print("See ratings for")
    options = ["1)Less than 30 episodes","2)About 100 episodes","3)About 200 episodes","4)More than 500 episodes","5)Exit"]
    for i in options:
        print(i)
    # loop until the user chooses the choice to quit the program
    while choice != 5:   
        # call the get_choice function to get the choice from the user and store in variable
        choice = check_choice(1,5)
        choice -= 1
        replys = ["The ratings of this option span from about 3 to 10","The ratings of this option span from about 4 to 10","The ratings of this option span from about 6 to 10","The ratings of this option span from about 6 to 10"]
        print(replys[choice])

def simple_visualizations():
    print("See type of visualization:")
    vis = ["1) Scatter","2)Line","3)Bar","4)Pie","5)Minimum Value","6)Maximum Value","7)Average Value","8)Exit"]
    for i in vis:
        print(i)
    #Simple visualization lists
    titles = ["Fullmetal Alchemist","Death Note","Cowboy Bepop","Bleach","Naruto","Neon Genesis Evangelion","Elfen Lied","Melancholy of Haruhi Suzumiya","Princess Mononoke","Spirited Away"]
    views = [23658,22279,21076,21003,18576,17961,17077,15711,15438,15434]
    ratings = [8.65,8.78,8.89,7.78,7.42,8.21,8.16,8.48,8.86,8.93]
    #function for scatter plot
    def scatter(x,y):
        plt.scatter(x,y)
        plt.title("Views vs Ratings")
        plt.xlabel("Views")
        plt.ylabel("Rating")
        plt.show()
        

    #function for line visual
    def line(x,y):
        plt.plot(x,y)
        plt.title("Ratings vs Views")
        plt.xlabel("Ratings")
        plt.ylabel("Views")
        plt.show()
        

    #function for bar chart
    def bar(x,y):
        plt.bar(x,y)
        plt.title("Views by anime")
        plt.xlabel("Anime")
        plt.ylabel("Views")
        plt.show()
        

    #function for pie chart
    def pie(views,y):
        plt.pie(views,labels = y)
        plt.title("Views by anime")
        plt.show()
        

    #function to determine minimum value
    def minimumVal(views,titles):
        least = views[0]
        anime = titles[0]
        for i in range(len(views)):
            if views[i]<least:
                least = views[i]
                anime = titles[i]
        return least, anime

    #function to determine maximum value
    def maximumVal(views,titles):
        most = views[0]
        anime = titles[0]
        for i in range(len(views)):
            if views[i]>most:
                most = views[i]
                anime = titles[i]
        return most, anime

    #function to determine average value
    def averageVal(views):
        total = 0
        for i in range(len(views)):
            total = total + views[i]
        avg = total/len(views)
        return avg
    choice = ''
    while choice != 8:
        choice = check_choice(1,8)
        if choice == 1:
            scatter(ratings,views)
        elif choice == 2:
            line(ratings,views)
        elif choice == 3:
            bar(views,titles)
        elif choice == 4:
            pie(views,titles)
        elif choice == 5:
            minVal, mintit = minimumVal(views,titles)
            print("The minimum amount of views in this list of anime is", minVal, "and is", mintit)
        elif choice == 6:
            maxVal,maxtit = maximumVal(views,titles)
            print("The maximum amount of views in this list of anime is", maxVal,"and is",maxtit)
        elif choice == 7:
            avgVal = averageVal(views)
            print("The avergae amount of views in this list of anime is", avgVal)
            
        
#Survey Analysis
def csvRead(filename):
    agel = []
    lengthl = []
    activel = []
    infile = open(filename,'r')
    line = infile.readline()
    line = line.strip()
    while line != "":
        time,age,watch,show,genre,length,active = line.split(',')
        agel.append(age)
        lengthl.append(length)
        activel.append(active)
        line = infile.readline()
        line = line.strip()
    agel.pop(0)
    lengthl.pop(0)
    activel.pop(0)
    return agel,lengthl,activel
#Check Age Function: checks if the age contains only digits OR that the first two characters contain only digits (i.e., 21yrs becomes 21) AND if the age is between 0 and 150
def checkAge(age):
    age1 = age
    ok = False
    while not ok:
        try:
            age = int(age)
            if age < 0 or age > 150:
                print("Age not in span of 0 to 150")
                ok = True
                return False
            else:
                ok = True
                return True
        except:
            c=0
            if age[0].isdigit():
                print("age is formatted to number")
                while age == age1 and c<len(age):
                    if age[c].isalpha():
                        age = age[:c]
                    else:
                        c = c + 1
            elif age[0].isalpha():
                print("age is not number")
                return False
            else:
                return True
    return True

#Check Linear Scale Function: checks if rating contains only digits and if the rating is between the specified scale 
def checkLinearScale(rating):
    rating1 = rating
    ok = False
    while not ok:
        try:
            rating = int(rating)
            if rating < 1 or rating > 5:
                print("Rating not in span of 1 to 5")
                return False
            else:
                ok = True
                return rating
        except:
            c=0
            while rating == rating1 and c<len(rating):
                if rating[c].isalpha():
                    rating = rating[:c]
                else:
                    c = c + 1

#Check Multiple Choice Function: checks if the choice for the multiple choice question is not empty and is one of the provided choices for the question
def checkMultipleChoice(choice):
    options = ['"<30 episodes"','"About 100 episodes"','"About 200 episodes"','">500 episodes"']
    pos = -1
    for i in range(len(options)):
        if choice == options[i]:
            pos = i
    if pos == -1:
        print("Option is invalid")
    else:
        return pos

#Linear Rating Plot: plots a histogram with the ratings for your linear scale question
def linearRatingPlot(list1):
    labels = "Rating 1", "Rating 2", "Rating 3", "Rating 4", "Rating 5"
    plt.hist(list1,5)
    plt.show()
    
#Counts Plot: plots a pie chart of the counts for each choice in the multiple choice question
def countPlot(opt1,opt2,opt3,opt4):
    options = "<30 episodes","About 100 episodes","About 200 episodes",">500 episodes"
    values = [opt1,opt2,opt3,opt4]
    plt.pie(values, labels = options)
    plt.show()
    
#Compute Function: computes a data statistic using the numpy module (i.e, mean, median, standard deviation) with the ratings for your linear scale question
def compute(ratings):
    mean = np.mean(ratings)
    median = np.median(ratings)
    std = np.std(ratings)
    return mean, median, std    
    
def clean(agel,lengthl,activel):
    print("#########################################################################")
    ratings = [0,0,0,0,0]
    choices = [0,0,0,0]
    for i in range(len(agel)):
        if checkAge(agel[i]):
            activel[i] = activel[i][1::2]
            if checkLinearScale(activel[i]) >0:
                activel[i] = int(activel[i])
                pos = activel[i]-1
                ratings[pos] = ratings[pos]+1
            choicePos = checkMultipleChoice(lengthl[i])
            choices[choicePos] = choices[choicePos] + 1
        else:
            print("Error on line", i)
    print("#########################################################################")
    return agel,lengthl,activel,choices,ratings
    
def survey_analysis(agel,lengthl,activel,choices):
    choice = ''
    while choice != 4:
        options = ["1)Histogram: Active Anime Watchers","2)Pie: Ratings of episodes","3)Computations","4)Quit"]
        for i in options:
            print(i)
        choice = check_choice(1,4)
        if choice == 1:
            linearRatingPlot(activel)
        elif choice == 2:
            countPlot(choices[0],choices[1],choices[2],choices[3])
        elif choice == 3:
            mean,median,std = compute(activel)
            print("The mean of how active anime watchers are is",mean)
            print("The median of how active anime watchers are is",median)
            print("The standard deviation of how active anime watchers are is",std)
    

#Data set analysis
def read_as_dataframe(filen):
    df = pd.read_csv(filen)
    return df

def clean_Dataframe(df):
    print("#########################################################################")
    df.drop(["synopsis", "img_url", "link"], axis=1, inplace=True)
    df = df.dropna(how='any',axis=0)
    print("Dropped unneeded columns")
    print("Dropped rows with missing values")
    print("#########################################################################")
    return df

def process_df(filen):
    df = read_as_dataframe(filen)
    df = clean_Dataframe(df)
    return df

def scatter(df):
    scat = df.plot.scatter(x='episodes', y='members', c='DarkBlue')
    plt.title("Episodes vs Members")
    plt.show()
    
# line chart
def line(df):
    lines = df.plot.line('episodes','score')
    plt.show()
    
# bar chart
def bar(table):
    x = table['episodes']
    y = table['score']
    plt.bar(x,y)
    
    #plt.xticks(rotation = 'vertical')
    
    plt.title("Episodes vs Score")
    plt.xlabel("Episodes")
    plt.ylabel("Score")
    
    plt.show()

def bars(df):
    table = pd.pivot_table(data=df, index='title', values=['popularity','episodes'], aggfunc='sum')
    x = table['episodes']
    y = table['popularity']
    plt.bar(x,y)
    plt.title("Episodes vs Popularity")
    plt.xlabel("Episodes")
    plt.ylabel("Poularity")
    plt.show()
    
def piv_sum_table(df):
    table = pd.pivot_table(data=df, index='title', values=['score','episodes'], aggfunc='sum')
    return table


def data_analysis(df):
    choice = ''
    while choice != 5:
        options = ["1)Scatter: Episodes vs Members","2)Line: Episodes vs Score","3)Bar: Popularity vs Episodes","4)Bar on Pivot Table: Episodes vs Score","5)Quit"]
        for i in options:
            print(i)
        table = piv_sum_table(df)
        choice = check_choice(1,5)
        if choice == 1:
            scatter(df)
        elif choice == 2:
            line(df)
        elif choice == 3:
            bars(df)
        elif choice == 4:
            bar(table)
            
def findings(df,activel,option1,option2,option3,option4):
    countPlot(option1,option2,option3,option4)
    print("With this visualization we can see a pie chart of the preferred amount of episodes of my survey respondents.")
    print("The most preferred length was that of about 100.")
    print('\n')
    linearRatingPlot(activel)
    print("In the linear rating visualization, we can see the majority of the respondents were heavy anime watchers.")
    print("With this info we have a general idea on how eduacted the respondents are with anime. We should keep this")
    print("in mid while looking at the other visualizations.")
    print('\n')
    table = piv_sum_table(df)
    bar(table)
    print("This visualization depicts the relationship between episodes and scores. Animes with high amounts of episodes")
    print("seem to be doing well regarding score. However most of the anime shown are have less than 100 episodes. There")
    print("is much more variety of scores with the lower amount of episodes.")
    print('\n')
    bars(df)
    print("This visualization shows the popularity against episodes. Anime with higher episodes also have a higher")
    print("popularity. This is similar to the previous visualization. Anime with less than 100 episodes have more")
    print("variety in poularity.")
    print('\n')
    print("I would say ultimately the number of episodes influences popularity and rating. However, it is not the")
    print("only influence. Anime with a large amount of episodes do very well, but with a lower amount of episodes")
    print("there is more variety in the scoring. Shows with less episodes need to compensate with better plot or")
    print("more popular genres.")
    print('\n')
    
###########################################################################################################
# END OF MENU OPTIONS 1 THRU. 8
###########################################################################################################    


###########################################################################################################
# START OF GETTING AND CHECKING USER INPUT CHOICE(S)
########################################################################################################### 

# function name: check_choice
# arguments: 2 integer values representing the minimum and maximum numbered options in the menu
# return: the valid input (i.e., a positive digit between the passed minimum and maximum arguments)
# description: asks the user for their choice and then checks that the user's input is a valid digit 
#              between the minimum and maximum arguments passed to it 
#              it keeps asking the for input until the user enters valid input (i.e., a positive digit 
#              between between the passed minimum and maximum arguments)
def check_choice(minimum, maximum):
    # define string variable that is empty to hold user's input
    some_input = ''
    
    # loop until the user's input is no longer empty
    while some_input == '':
        # ask the user to input their choice and store in a variable
        some_input = input('Choice: ')
        
        # check if the user's input does not contain only digits
        if some_input.isdigit() == False:
            # output an error message stating that the user did not enter input with only digits
            print('\nYou did not enter input with only digits! Try again.\n')
        
        # otherwise (i.e., the user's input contains only digits)
        else:
            # convert the user's input to an integer
            # "1" --> 1
            some_input = int(some_input)

            # check if the user's input is less than the minimum or greater than the maximum
            if some_input < minimum or some_input > maximum:
                # output an error message stating that the user did not enter input between 1 and 5
                print('\nYou did not enter a valid choice. Choose any option from ' + str(minimum) + ' to ' + str(maximum) + '.\n')
    
    # return the user's input 
    return some_input


# function name: get_choice
# arguments: none
# return: the valid input (i.e., a positive digit between 1 and 5)
# description: outputs the list of five choices for the main menu and calls the check_choice function 
#              passing it 1 as the minimum and 5 as the maximum to obtain a valid input from the user 
def get_choice():
    # output the list of options the user can choose from
    # choice 1 --> Overview of the [YOUR DATA SET NAME] Data Set
    # choice 2 --> Data-Driven Questions and Predictions
    # choice 3 --> Basic Statistics on [YOUR DATA SET NAME]
    # choice 4 --> Simple Data Visualizations on [YOUR DATA SET NAME]
    # choice 5 --> Survey Analysis
    # choice 6 --> Data Set Analysis
    # choice 7 --> Findings and Observations
    # choice 8 --> Quit
    print('Choose one of the options below to view the data analysis for this data set and its data-driven question.\n')    
    
    print('1. Overview of the Anime Data Set')
    print('2. Data-Driven Questions and Predictions')
    print('3. Basic Statistics on Anime')
    print('4. Simple Data Visualizations on Anime')
    print('5. Survey Analysis')
    print('6. Data Set Analysis')
    print('7. Findings and Observations')
    print('8. Quit.\n')
    
    
    # call the check_choice function passing it 1 as the minimum and 8 as the maximum
    #      store the returned value in a variable
    choice = check_choice(1, 8)
     
        
    # return the user's input that was stored in the variable above
    return choice

###########################################################################################################
# END OF GETTING AND CHECKING USER INPUT CHOICE(S)
########################################################################################################### 


###########################################################################################################
# START OF SETUP --> WELCOME MESSAGE AND MAIN FUNCTION
###########################################################################################################

# function name: welcome_msg
# arguments: none
# return: none
# description: outputs the title of the program and where the data was collected from (i.e., website, data set)
def welcome_msg():
    dq = 'Is their a connection between the duration of a series and its rating?'
    
    print('\t\t\t\t\tAnime: ')
    print('\t\t\t\t' + dq.upper())
    print('\n')
    print('\t\t\tWelcome to the Anime data set analysis program!\n')


# function name: main
# arguments: none
# return: none
# description: setups the program and manages calls to other functions defined to handle the eight options
#              it repeats the eight options until the user chooses the option to quit
def main():
    # call welcome_msg function to output the title of the program and where the data was collected from
    welcome_msg()
    
    
    # flag variable keeping track of if the survey data has already been processed/cleaned
    #      assume at the beginning of program that survey data has NOT been processed/cleaned
    #      update this flag variable when the 5th or 7th option have been chosen for the first time
    survey_processed = False
    
    
    # flag variable keeping track of if the DataFrame containing the data from your data set you found online 
    #      has already been processed/cleaned
    #      assume at the beginning of program that DataFrame has NOT been processed/cleaned
    #      update this flag variable when the 6th or 7th option have been chosen for the first time
    data_processed = False
    
    
    # define string variable that is empty to hold user's input
    choice = ''
    

    # loop until the user chooses the choice to quit the program
    while choice != 8:
        
        # call the get_choice function to get the choice from the user and store in variable
        choice = get_choice()
        
        # check if the user chose the first option
        if choice == 1:
            # call overview function to output an overview of your topic and data set
            overview()
        elif choice == 2:
            dq()
        elif choice == 3:
            basic_stats()
        elif choice == 4:
            simple_visualizations()
        elif choice == 5 or choice == 6 or choice == 7:
            if not survey_processed:
                agel,lengthl,activel = csvRead('Anime Survey.csv')
                agel,lengthl,activel,choices,ratings = clean(agel,lengthl,activel)
            if not data_processed:
                df = process_df('animes.csv')
            if choice == 5:
                survey_analysis(agel,lengthl,activel,choices)
            elif choice == 6:
                data_analysis(df)
            elif choice == 7:
                option1 = choices[0]
                option2 = choices[1]
                option3 = choices[2]
                option4 = choices[3]
                findings(df,activel,option1,option2,option3,option4)
            

        
###########################################################################################################
# END OF SETUP --> WELCOME MESSAGE AND MAIN FUNCTION
###########################################################################################################



# call the main function to run your program  
main()


# In[ ]:





# In[ ]:




