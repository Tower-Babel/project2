import streamlit as st
from PIL import Image

st.title(" :blue[Project 2:] ")
st.title(" :blue[Optiver - Trading at the Close] ")


image1 = Image.open("/project2/Picture1.png")
image2 = Image.open("project2/Picture2.png")
image3 = Image.open("project2/Picture3.png")
image4 = Image.open("project2/Picture4.png")
image5 = Image.open("project2/Picture5.png")
image6 = Image.open("project2/Picture6.png")
image7 = Image.open("project2/Picture7.png")
image8 = Image.open("project2/Picture8.png")
image9 = Image.open("project2/Picture9.png")
image10 = Image.open("project2/Picture10.png")

st.header("Introduce the Problem")
st.write(
    """

    This project aims to find opportunities in the stock market. The ability to consolidate and predict prices create an competitive edge. 
    We aim to develop a model capable of predicting the closing movements of hundreds of stocks. 
    #
    Stock exchanges are fast-paced and complex. The ability to consolidate and predict prices gives other market makers, traders, quantitative researchers and engineers an edge.

    The data comes from Kaggle competition 
    (Optiver Trading at the close https://www.kaggle.com/competitions/optiver-trading-at-the-close/overview) 
    



    """
)

st.header("Introduce the Data")
st.write(

"""
    This data and description comes from kaggle code competition - Optiver Trading at the close https://www.kaggle.com/competitions/optiver-trading-at-the-close/overview

    
    The dataset contains historic data of the NASDAQ stock exchange. "Column definitions".

    
    Lets look at the rows and columns description that was provided:

    - stock_id - Is a unique identifier for the stock. Not all stock ID's exist in every time bucket
    - date_id - Is a unique identifier for the date. Zero null values
    - inbalance_size - Is the amount unmatched at the current reference price (in USD)
        - buy-side imbalance; one
        - sell-side imbalance; -1
        - no imbalance; zero
        
    - matched_size - The amount that can be matched at the current reference price
    - far_price - The crossing price that will max the number of shares matched based on auction interest only
    - near_price - The price that will max the number of shares matched based auction and continuous market orders
    - [bid/ask]_price - Price of the most competitive buy/sell level in the non auction book
    - [bid/ask]_size - The dollar amount on the most competitive buy/sell level in the non-auction book
    - wap - The weighted average price in the non-auction book (WAP is a fair guess for the price of a stock.)
    - target -  The 60 second future move in the wap of the stock    
    The concept around trading at the close is not quite simple. For Nasdaq Closing auctions,
      the exchange accepts orders at the start of the trading day and begins to publish the state of the
        auction at 3:50pm Eastern Time, which is 10 mins before the market closes. 
        The closing price in the auction is determined as the price which the maximum number of shares can be matched.

        
"""

)

st.image(image1, caption=None)
#st.image(image2, caption=None)
st.write(
    
    """
         Takeaway: We have 200 stock ids and 481 trading days. All columns are numeric. Not all stocks get traded on each day. There seem to be outliers
    """
)

st.header("Pre-processing the Data")
st.write(
"""    

    From the above dataframe we can see the rows that contain null values and missing data. 
    We will use binary flags, 0 and 1 for missing data.
    We can use a sample from the set to visualize the orderbook for a single stock. We will need the bid size, price and ask size. We can also use bid size and ask size to make features to train our model on.
"""
)




st.image(image2, caption=None)
st.header("Data Understanding/Visualization")
st.write(
    """

    To understand the data mode we can say have a big trading board where each person has written down on the board what they 
    want to buy and how much they are willing to pay. They also written down how much they want to 
    sell and the price at which they are selling. 
    Now all these items are on display. We can see that some people want to buy at lower price (0.99)
    as soon as the market opens but after 1 minute passes, people offer to buy at a higher price (1.0). 
    The auction book keeps track of buying and selling in one place. When a buyer comes and say they want to 
    buy 1 stock at 1 dollar, the board checks if there's anyone who wants to sell at 1 dollar and they made the deal and 
    the stock changes hands. The auction book helps everyone know what cards are available and at what price. 
    It is a big organized list that keeps track of things. 

    #


    """
)
st.image(image5, caption=None)

st.write(
    """

    Lets visualize the bid/ask and WAP relationship.
    """
)

st.image(image3, caption=None)
st.image(image4, caption=None)
st.write(
    """
     
    If the bid size increases the buyers are more aggressive so the bid price should be closer to the ask price. 

    Interesting Fact: In an Auction Order Book, the orders are collected but not immediately matched until the auction ends (3:50pm).
    Suppose the auction ends with the book in this state then a price of 1.0 the 373,331 lots will be matched

    Lets look at a smaller example.

    """

)


st.image(image6, caption=None)
st.write(
    """
    - At a price of 10, 0 lots would be matched, as there are no bids greater than or equal to 10
    - At a price of 9, 5 lots would be matched, as there are five bids greater than or equal to 9 and 6 asks less than or equal to 9
    - At a price of 8, 4 lots would be matched

    So, the price which maximizes matched lots would be the price of nine. We would now describe the price of nine as the uncross price and the match size is five and the imbalance would be 1 lot in the sell direction. The term **near price** comes from the price of where the max number of lots can be matched.

    - If the near price is between the best bid and ask, then the reference price is equal to the near price
    - If the near price is > best ask, then reference price = best ask
    - If the near price < best bid, then reference price = best bid. The reference price is the near price bounded between the bid and ask

    

    """
)

st.header("Modeling")
st.write(
    """
    To perform classification such as: Logistic Regression, Random Forest and Gradient Boosting, we will need to split our data. We need to categorize data points into predefined classes or categories. The simple category of the Trading at close data would be up or down. That is categorize stocks as increasing or decreasing. We can use multiple shallow decision trees to make better predictions to prevent overfitting.

    We will use Light Gradient Boost - LightGBM which is a decision tree boosting algorithm that takes the dataset attributes and puts them into discrete bins. LightGBM grows trees leaf-wise by choosing the lead with the max delta loss to grow.

    Gradient Boost starts by making a single leaf after making a guess. And it builds fix sized tree and scales the tree.

    The first thing we do is calculate the average price and the ratio in bid_size and ask_size. As well as the ratio in imbalance size compared to matched size. The ratio will help us in analyzing the supply and demand. We will then use this ratio to get insights into the demand at each price point and then we will train our model on this feature.

        
    """

)
st.image(image8, caption=None)
st.image(image9, caption=None)
st.image(image10, caption=None)


st.header("Evaluation")
st.write(
    """
    The initial Classification method was overfitted. With only 1 tree, the predictions were mostly "Up". Do to overfitting.

    To acheive better performance we used ensemble method that combine predicitons of several models. 
    This method goes through cycles to iteratively add models into an ensemble. 
    Predictions are made by add all models predictions into the ensemble. These predictions are used to calculate the loss funtion Mean Squared Error. 
    Then the loss funtion is used to fit a new model.
    An ensemble method was used and MAE was used to compare the predicted price for model performance.

    MAE improvement in basis points: A lower MAE indicates better model performance. 
    When the MAE is small, it means that, on average and the model's predictions are very close to the actual values. 
    But a higher MAE indicates that the model's predictions have larger errors.

    """
)

st.header("Storytelling")
st.write(
    """
    Here the model is comparing each node based on the provided features.

    - The model splits the data based on the number seconds elapsed
    - It compares buy_sell flag
    - It compares reference_price
    - It compares the derived features such as the ratio in imb_s1


    - If the bid size is significantly larger than the ask size, it can indicate a good strong buy interest while opposite could suggest strong selling interest. This can be used to capture price changes

    - When imbalance is combined with the ratio of imbalance it can show the pressure on the market. A large imbalance can indicate price movement.

    These provide insights to capture the relationships between different relationship aspects of the order book data and used to predict stock price movement.

    """

)

st.header("Impact")
st.write(
    """
Overall, the hope is that these features will provide some information for making predictions or decisions related to the stocks. 
A simple baseline is to assume we have no valuable information about the direction any stock moves, which translates to a predicted value of 0 for all observations. This baseline is quite hard to beat in the context of financial markets.

However, we have some information in our dataset that should help us to beat this baseline. If we observe an auction imbalance, 
it indicates that at the current price there is buying or selling interest that will currently not get matched in the auction. 
We can therefore adjust our prediction upwards if there is a buy imbalance & downwards if there is a sell imbalance. 

- 0 means there is no direction
- less than 0 means sell imbalance and downwards 
- greater than 0 means buy imbalance and upwards


    """
)

st.header("References")
st.write(
    """
        References:
    1. https://www.kaggle.com/code/yuanzhezhou/baseline-lgb-xgb-and-catboost //Yuanzhe Zhou's code
    2. https://www.kaggle.com/code/renatoreggiani/optv-lightgbm
    3. https://www.kaggle.com/code/kaito510/goto-conversion-optiver-baseline-models
    4. https://www.kaggle.com/code/iqbalsyahakbar/optiver-a-starter-s-notebook
    """

)

st.header("Code")
st.write("https://www.kaggle.com/code/august33rd/project2/")
