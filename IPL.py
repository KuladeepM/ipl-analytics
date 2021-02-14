{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# M R Kuladeep"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 204,
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "import numpy as np"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Reading the file"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {},
   "outputs": [],
   "source": [
    "data = pd.read_csv('Desktop\\matches.csv')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 296,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>id</th>\n",
       "      <th>season</th>\n",
       "      <th>city</th>\n",
       "      <th>date</th>\n",
       "      <th>team1</th>\n",
       "      <th>team2</th>\n",
       "      <th>toss_winner</th>\n",
       "      <th>toss_decision</th>\n",
       "      <th>result</th>\n",
       "      <th>dl_applied</th>\n",
       "      <th>winner</th>\n",
       "      <th>win_by_runs</th>\n",
       "      <th>win_by_wickets</th>\n",
       "      <th>player_of_match</th>\n",
       "      <th>venue</th>\n",
       "      <th>umpire1</th>\n",
       "      <th>umpire2</th>\n",
       "      <th>umpire3</th>\n",
       "      <th>match_id</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>751</th>\n",
       "      <td>11347</td>\n",
       "      <td>2019</td>\n",
       "      <td>Mumbai</td>\n",
       "      <td>05/05/19</td>\n",
       "      <td>Kolkata Knight Riders</td>\n",
       "      <td>Mumbai Indians</td>\n",
       "      <td>Mumbai Indians</td>\n",
       "      <td>field</td>\n",
       "      <td>normal</td>\n",
       "      <td>0</td>\n",
       "      <td>Mumbai Indians</td>\n",
       "      <td>0</td>\n",
       "      <td>9</td>\n",
       "      <td>HH Pandya</td>\n",
       "      <td>Wankhede Stadium</td>\n",
       "      <td>Nanda Kishore</td>\n",
       "      <td>O Nandan</td>\n",
       "      <td>S Ravi</td>\n",
       "      <td>11347</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>752</th>\n",
       "      <td>11412</td>\n",
       "      <td>2019</td>\n",
       "      <td>Chennai</td>\n",
       "      <td>07/05/19</td>\n",
       "      <td>Chennai Super Kings</td>\n",
       "      <td>Mumbai Indians</td>\n",
       "      <td>Chennai Super Kings</td>\n",
       "      <td>bat</td>\n",
       "      <td>normal</td>\n",
       "      <td>0</td>\n",
       "      <td>Mumbai Indians</td>\n",
       "      <td>0</td>\n",
       "      <td>6</td>\n",
       "      <td>AS Yadav</td>\n",
       "      <td>M. A. Chidambaram Stadium</td>\n",
       "      <td>Nigel Llong</td>\n",
       "      <td>Nitin Menon</td>\n",
       "      <td>Ian Gould</td>\n",
       "      <td>11412</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>753</th>\n",
       "      <td>11413</td>\n",
       "      <td>2019</td>\n",
       "      <td>Visakhapatnam</td>\n",
       "      <td>08/05/19</td>\n",
       "      <td>Sunrisers Hyderabad</td>\n",
       "      <td>Delhi Capitals</td>\n",
       "      <td>Delhi Capitals</td>\n",
       "      <td>field</td>\n",
       "      <td>normal</td>\n",
       "      <td>0</td>\n",
       "      <td>Delhi Capitals</td>\n",
       "      <td>0</td>\n",
       "      <td>2</td>\n",
       "      <td>RR Pant</td>\n",
       "      <td>ACA-VDCA Stadium</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>11413</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>754</th>\n",
       "      <td>11414</td>\n",
       "      <td>2019</td>\n",
       "      <td>Visakhapatnam</td>\n",
       "      <td>10/05/19</td>\n",
       "      <td>Delhi Capitals</td>\n",
       "      <td>Chennai Super Kings</td>\n",
       "      <td>Chennai Super Kings</td>\n",
       "      <td>field</td>\n",
       "      <td>normal</td>\n",
       "      <td>0</td>\n",
       "      <td>Chennai Super Kings</td>\n",
       "      <td>0</td>\n",
       "      <td>6</td>\n",
       "      <td>F du Plessis</td>\n",
       "      <td>ACA-VDCA Stadium</td>\n",
       "      <td>Sundaram Ravi</td>\n",
       "      <td>Bruce Oxenford</td>\n",
       "      <td>Chettithody Shamshuddin</td>\n",
       "      <td>11414</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>755</th>\n",
       "      <td>11415</td>\n",
       "      <td>2019</td>\n",
       "      <td>Hyderabad</td>\n",
       "      <td>12/05/19</td>\n",
       "      <td>Mumbai Indians</td>\n",
       "      <td>Chennai Super Kings</td>\n",
       "      <td>Mumbai Indians</td>\n",
       "      <td>bat</td>\n",
       "      <td>normal</td>\n",
       "      <td>0</td>\n",
       "      <td>Mumbai Indians</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>JJ Bumrah</td>\n",
       "      <td>Rajiv Gandhi Intl. Cricket Stadium</td>\n",
       "      <td>Nitin Menon</td>\n",
       "      <td>Ian Gould</td>\n",
       "      <td>Nigel Llong</td>\n",
       "      <td>11415</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "        id  season           city      date                  team1  \\\n",
       "751  11347    2019         Mumbai  05/05/19  Kolkata Knight Riders   \n",
       "752  11412    2019        Chennai  07/05/19    Chennai Super Kings   \n",
       "753  11413    2019  Visakhapatnam  08/05/19    Sunrisers Hyderabad   \n",
       "754  11414    2019  Visakhapatnam  10/05/19         Delhi Capitals   \n",
       "755  11415    2019      Hyderabad  12/05/19         Mumbai Indians   \n",
       "\n",
       "                   team2          toss_winner toss_decision  result  \\\n",
       "751       Mumbai Indians       Mumbai Indians         field  normal   \n",
       "752       Mumbai Indians  Chennai Super Kings           bat  normal   \n",
       "753       Delhi Capitals       Delhi Capitals         field  normal   \n",
       "754  Chennai Super Kings  Chennai Super Kings         field  normal   \n",
       "755  Chennai Super Kings       Mumbai Indians           bat  normal   \n",
       "\n",
       "     dl_applied               winner  win_by_runs  win_by_wickets  \\\n",
       "751           0       Mumbai Indians            0               9   \n",
       "752           0       Mumbai Indians            0               6   \n",
       "753           0       Delhi Capitals            0               2   \n",
       "754           0  Chennai Super Kings            0               6   \n",
       "755           0       Mumbai Indians            1               0   \n",
       "\n",
       "    player_of_match                               venue        umpire1  \\\n",
       "751       HH Pandya                    Wankhede Stadium  Nanda Kishore   \n",
       "752        AS Yadav           M. A. Chidambaram Stadium    Nigel Llong   \n",
       "753         RR Pant                    ACA-VDCA Stadium            NaN   \n",
       "754    F du Plessis                    ACA-VDCA Stadium  Sundaram Ravi   \n",
       "755       JJ Bumrah  Rajiv Gandhi Intl. Cricket Stadium    Nitin Menon   \n",
       "\n",
       "            umpire2                  umpire3  match_id  \n",
       "751        O Nandan                   S Ravi     11347  \n",
       "752     Nitin Menon                Ian Gould     11412  \n",
       "753             NaN                      NaN     11413  \n",
       "754  Bruce Oxenford  Chettithody Shamshuddin     11414  \n",
       "755       Ian Gould              Nigel Llong     11415  "
      ]
     },
     "execution_count": 296,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data.tail()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "metadata": {},
   "outputs": [],
   "source": [
    "data=data.dropna(how='all')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>id</th>\n",
       "      <th>season</th>\n",
       "      <th>city</th>\n",
       "      <th>date</th>\n",
       "      <th>team1</th>\n",
       "      <th>team2</th>\n",
       "      <th>toss_winner</th>\n",
       "      <th>toss_decision</th>\n",
       "      <th>result</th>\n",
       "      <th>dl_applied</th>\n",
       "      <th>winner</th>\n",
       "      <th>win_by_runs</th>\n",
       "      <th>win_by_wickets</th>\n",
       "      <th>player_of_match</th>\n",
       "      <th>venue</th>\n",
       "      <th>umpire1</th>\n",
       "      <th>umpire2</th>\n",
       "      <th>umpire3</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>1</td>\n",
       "      <td>2017</td>\n",
       "      <td>Hyderabad</td>\n",
       "      <td>2017-04-05</td>\n",
       "      <td>Sunrisers Hyderabad</td>\n",
       "      <td>Royal Challengers Bangalore</td>\n",
       "      <td>Royal Challengers Bangalore</td>\n",
       "      <td>field</td>\n",
       "      <td>normal</td>\n",
       "      <td>0</td>\n",
       "      <td>Sunrisers Hyderabad</td>\n",
       "      <td>35</td>\n",
       "      <td>0</td>\n",
       "      <td>Yuvraj Singh</td>\n",
       "      <td>Rajiv Gandhi International Stadium, Uppal</td>\n",
       "      <td>AY Dandekar</td>\n",
       "      <td>NJ Llong</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>2</td>\n",
       "      <td>2017</td>\n",
       "      <td>Pune</td>\n",
       "      <td>2017-04-06</td>\n",
       "      <td>Mumbai Indians</td>\n",
       "      <td>Rising Pune Supergiant</td>\n",
       "      <td>Rising Pune Supergiant</td>\n",
       "      <td>field</td>\n",
       "      <td>normal</td>\n",
       "      <td>0</td>\n",
       "      <td>Rising Pune Supergiant</td>\n",
       "      <td>0</td>\n",
       "      <td>7</td>\n",
       "      <td>SPD Smith</td>\n",
       "      <td>Maharashtra Cricket Association Stadium</td>\n",
       "      <td>A Nand Kishore</td>\n",
       "      <td>S Ravi</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>3</td>\n",
       "      <td>2017</td>\n",
       "      <td>Rajkot</td>\n",
       "      <td>2017-04-07</td>\n",
       "      <td>Gujarat Lions</td>\n",
       "      <td>Kolkata Knight Riders</td>\n",
       "      <td>Kolkata Knight Riders</td>\n",
       "      <td>field</td>\n",
       "      <td>normal</td>\n",
       "      <td>0</td>\n",
       "      <td>Kolkata Knight Riders</td>\n",
       "      <td>0</td>\n",
       "      <td>10</td>\n",
       "      <td>CA Lynn</td>\n",
       "      <td>Saurashtra Cricket Association Stadium</td>\n",
       "      <td>Nitin Menon</td>\n",
       "      <td>CK Nandan</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>4</td>\n",
       "      <td>2017</td>\n",
       "      <td>Indore</td>\n",
       "      <td>2017-04-08</td>\n",
       "      <td>Rising Pune Supergiant</td>\n",
       "      <td>Kings XI Punjab</td>\n",
       "      <td>Kings XI Punjab</td>\n",
       "      <td>field</td>\n",
       "      <td>normal</td>\n",
       "      <td>0</td>\n",
       "      <td>Kings XI Punjab</td>\n",
       "      <td>0</td>\n",
       "      <td>6</td>\n",
       "      <td>GJ Maxwell</td>\n",
       "      <td>Holkar Cricket Stadium</td>\n",
       "      <td>AK Chaudhary</td>\n",
       "      <td>C Shamshuddin</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>5</td>\n",
       "      <td>2017</td>\n",
       "      <td>Bangalore</td>\n",
       "      <td>2017-04-08</td>\n",
       "      <td>Royal Challengers Bangalore</td>\n",
       "      <td>Delhi Daredevils</td>\n",
       "      <td>Royal Challengers Bangalore</td>\n",
       "      <td>bat</td>\n",
       "      <td>normal</td>\n",
       "      <td>0</td>\n",
       "      <td>Royal Challengers Bangalore</td>\n",
       "      <td>15</td>\n",
       "      <td>0</td>\n",
       "      <td>KM Jadhav</td>\n",
       "      <td>M Chinnaswamy Stadium</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   id  season       city        date                        team1  \\\n",
       "0   1    2017  Hyderabad  2017-04-05          Sunrisers Hyderabad   \n",
       "1   2    2017       Pune  2017-04-06               Mumbai Indians   \n",
       "2   3    2017     Rajkot  2017-04-07                Gujarat Lions   \n",
       "3   4    2017     Indore  2017-04-08       Rising Pune Supergiant   \n",
       "4   5    2017  Bangalore  2017-04-08  Royal Challengers Bangalore   \n",
       "\n",
       "                         team2                  toss_winner toss_decision  \\\n",
       "0  Royal Challengers Bangalore  Royal Challengers Bangalore         field   \n",
       "1       Rising Pune Supergiant       Rising Pune Supergiant         field   \n",
       "2        Kolkata Knight Riders        Kolkata Knight Riders         field   \n",
       "3              Kings XI Punjab              Kings XI Punjab         field   \n",
       "4             Delhi Daredevils  Royal Challengers Bangalore           bat   \n",
       "\n",
       "   result  dl_applied                       winner  win_by_runs  \\\n",
       "0  normal           0          Sunrisers Hyderabad           35   \n",
       "1  normal           0       Rising Pune Supergiant            0   \n",
       "2  normal           0        Kolkata Knight Riders            0   \n",
       "3  normal           0              Kings XI Punjab            0   \n",
       "4  normal           0  Royal Challengers Bangalore           15   \n",
       "\n",
       "   win_by_wickets player_of_match                                      venue  \\\n",
       "0               0    Yuvraj Singh  Rajiv Gandhi International Stadium, Uppal   \n",
       "1               7       SPD Smith    Maharashtra Cricket Association Stadium   \n",
       "2              10         CA Lynn     Saurashtra Cricket Association Stadium   \n",
       "3               6      GJ Maxwell                     Holkar Cricket Stadium   \n",
       "4               0       KM Jadhav                      M Chinnaswamy Stadium   \n",
       "\n",
       "          umpire1        umpire2 umpire3  \n",
       "0     AY Dandekar       NJ Llong     NaN  \n",
       "1  A Nand Kishore         S Ravi     NaN  \n",
       "2     Nitin Menon      CK Nandan     NaN  \n",
       "3    AK Chaudhary  C Shamshuddin     NaN  \n",
       "4             NaN            NaN     NaN  "
      ]
     },
     "execution_count": 21,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data.head()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Most successful Teams"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "metadata": {},
   "outputs": [],
   "source": [
    "success = data['winner'].groupby(data['winner']).count()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "winner\n",
       "Mumbai Indians                 109\n",
       "Chennai Super Kings            100\n",
       "Kolkata Knight Riders           92\n",
       "Royal Challengers Bangalore     84\n",
       "Kings XI Punjab                 82\n",
       "Rajasthan Royals                75\n",
       "Delhi Daredevils                67\n",
       "Sunrisers Hyderabad             58\n",
       "Deccan Chargers                 29\n",
       "Gujarat Lions                   13\n",
       "Pune Warriors                   12\n",
       "Rising Pune Supergiant          10\n",
       "Delhi Capitals                  10\n",
       "Kochi Tuskers Kerala             6\n",
       "Rising Pune Supergiants          5\n",
       "Name: winner, dtype: int64"
      ]
     },
     "execution_count": 23,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "success.sort_values(ascending=False)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Successful team in 2017"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "metadata": {},
   "outputs": [],
   "source": [
    "s17 = data[data['season']==2017]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "metadata": {
    "scrolled": false
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>id</th>\n",
       "      <th>season</th>\n",
       "      <th>city</th>\n",
       "      <th>date</th>\n",
       "      <th>team1</th>\n",
       "      <th>team2</th>\n",
       "      <th>toss_winner</th>\n",
       "      <th>toss_decision</th>\n",
       "      <th>result</th>\n",
       "      <th>dl_applied</th>\n",
       "      <th>winner</th>\n",
       "      <th>win_by_runs</th>\n",
       "      <th>win_by_wickets</th>\n",
       "      <th>player_of_match</th>\n",
       "      <th>venue</th>\n",
       "      <th>umpire1</th>\n",
       "      <th>umpire2</th>\n",
       "      <th>umpire3</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>1</td>\n",
       "      <td>2017</td>\n",
       "      <td>Hyderabad</td>\n",
       "      <td>2017-04-05</td>\n",
       "      <td>Sunrisers Hyderabad</td>\n",
       "      <td>Royal Challengers Bangalore</td>\n",
       "      <td>Royal Challengers Bangalore</td>\n",
       "      <td>field</td>\n",
       "      <td>normal</td>\n",
       "      <td>0</td>\n",
       "      <td>Sunrisers Hyderabad</td>\n",
       "      <td>35</td>\n",
       "      <td>0</td>\n",
       "      <td>Yuvraj Singh</td>\n",
       "      <td>Rajiv Gandhi International Stadium, Uppal</td>\n",
       "      <td>AY Dandekar</td>\n",
       "      <td>NJ Llong</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>2</td>\n",
       "      <td>2017</td>\n",
       "      <td>Pune</td>\n",
       "      <td>2017-04-06</td>\n",
       "      <td>Mumbai Indians</td>\n",
       "      <td>Rising Pune Supergiant</td>\n",
       "      <td>Rising Pune Supergiant</td>\n",
       "      <td>field</td>\n",
       "      <td>normal</td>\n",
       "      <td>0</td>\n",
       "      <td>Rising Pune Supergiant</td>\n",
       "      <td>0</td>\n",
       "      <td>7</td>\n",
       "      <td>SPD Smith</td>\n",
       "      <td>Maharashtra Cricket Association Stadium</td>\n",
       "      <td>A Nand Kishore</td>\n",
       "      <td>S Ravi</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>3</td>\n",
       "      <td>2017</td>\n",
       "      <td>Rajkot</td>\n",
       "      <td>2017-04-07</td>\n",
       "      <td>Gujarat Lions</td>\n",
       "      <td>Kolkata Knight Riders</td>\n",
       "      <td>Kolkata Knight Riders</td>\n",
       "      <td>field</td>\n",
       "      <td>normal</td>\n",
       "      <td>0</td>\n",
       "      <td>Kolkata Knight Riders</td>\n",
       "      <td>0</td>\n",
       "      <td>10</td>\n",
       "      <td>CA Lynn</td>\n",
       "      <td>Saurashtra Cricket Association Stadium</td>\n",
       "      <td>Nitin Menon</td>\n",
       "      <td>CK Nandan</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>4</td>\n",
       "      <td>2017</td>\n",
       "      <td>Indore</td>\n",
       "      <td>2017-04-08</td>\n",
       "      <td>Rising Pune Supergiant</td>\n",
       "      <td>Kings XI Punjab</td>\n",
       "      <td>Kings XI Punjab</td>\n",
       "      <td>field</td>\n",
       "      <td>normal</td>\n",
       "      <td>0</td>\n",
       "      <td>Kings XI Punjab</td>\n",
       "      <td>0</td>\n",
       "      <td>6</td>\n",
       "      <td>GJ Maxwell</td>\n",
       "      <td>Holkar Cricket Stadium</td>\n",
       "      <td>AK Chaudhary</td>\n",
       "      <td>C Shamshuddin</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>5</td>\n",
       "      <td>2017</td>\n",
       "      <td>Bangalore</td>\n",
       "      <td>2017-04-08</td>\n",
       "      <td>Royal Challengers Bangalore</td>\n",
       "      <td>Delhi Daredevils</td>\n",
       "      <td>Royal Challengers Bangalore</td>\n",
       "      <td>bat</td>\n",
       "      <td>normal</td>\n",
       "      <td>0</td>\n",
       "      <td>Royal Challengers Bangalore</td>\n",
       "      <td>15</td>\n",
       "      <td>0</td>\n",
       "      <td>KM Jadhav</td>\n",
       "      <td>M Chinnaswamy Stadium</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   id  season       city        date                        team1  \\\n",
       "0   1    2017  Hyderabad  2017-04-05          Sunrisers Hyderabad   \n",
       "1   2    2017       Pune  2017-04-06               Mumbai Indians   \n",
       "2   3    2017     Rajkot  2017-04-07                Gujarat Lions   \n",
       "3   4    2017     Indore  2017-04-08       Rising Pune Supergiant   \n",
       "4   5    2017  Bangalore  2017-04-08  Royal Challengers Bangalore   \n",
       "\n",
       "                         team2                  toss_winner toss_decision  \\\n",
       "0  Royal Challengers Bangalore  Royal Challengers Bangalore         field   \n",
       "1       Rising Pune Supergiant       Rising Pune Supergiant         field   \n",
       "2        Kolkata Knight Riders        Kolkata Knight Riders         field   \n",
       "3              Kings XI Punjab              Kings XI Punjab         field   \n",
       "4             Delhi Daredevils  Royal Challengers Bangalore           bat   \n",
       "\n",
       "   result  dl_applied                       winner  win_by_runs  \\\n",
       "0  normal           0          Sunrisers Hyderabad           35   \n",
       "1  normal           0       Rising Pune Supergiant            0   \n",
       "2  normal           0        Kolkata Knight Riders            0   \n",
       "3  normal           0              Kings XI Punjab            0   \n",
       "4  normal           0  Royal Challengers Bangalore           15   \n",
       "\n",
       "   win_by_wickets player_of_match                                      venue  \\\n",
       "0               0    Yuvraj Singh  Rajiv Gandhi International Stadium, Uppal   \n",
       "1               7       SPD Smith    Maharashtra Cricket Association Stadium   \n",
       "2              10         CA Lynn     Saurashtra Cricket Association Stadium   \n",
       "3               6      GJ Maxwell                     Holkar Cricket Stadium   \n",
       "4               0       KM Jadhav                      M Chinnaswamy Stadium   \n",
       "\n",
       "          umpire1        umpire2 umpire3  \n",
       "0     AY Dandekar       NJ Llong     NaN  \n",
       "1  A Nand Kishore         S Ravi     NaN  \n",
       "2     Nitin Menon      CK Nandan     NaN  \n",
       "3    AK Chaudhary  C Shamshuddin     NaN  \n",
       "4             NaN            NaN     NaN  "
      ]
     },
     "execution_count": 25,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "s17.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "metadata": {},
   "outputs": [],
   "source": [
    "ss17=s17['winner'].groupby(s17['winner']).count()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "winner\n",
       "Mumbai Indians                 12\n",
       "Rising Pune Supergiant         10\n",
       "Kolkata Knight Riders           9\n",
       "Sunrisers Hyderabad             8\n",
       "Kings XI Punjab                 7\n",
       "Delhi Daredevils                6\n",
       "Gujarat Lions                   4\n",
       "Royal Challengers Bangalore     3\n",
       "Name: winner, dtype: int64"
      ]
     },
     "execution_count": 27,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "ss17.sort_values(ascending=False)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Players with most man of the matches"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "metadata": {},
   "outputs": [],
   "source": [
    "M=data['player_of_match'].groupby(data['player_of_match']).count()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "player_of_match\n",
       "CH Gayle          21\n",
       "AB de Villiers    20\n",
       "MS Dhoni          17\n",
       "DA Warner         17\n",
       "RG Sharma         17\n",
       "YK Pathan         16\n",
       "SR Watson         15\n",
       "SK Raina          14\n",
       "G Gambhir         13\n",
       "V Kohli           12\n",
       "Name: player_of_match, dtype: int64"
      ]
     },
     "execution_count": 29,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "M.sort_values(ascending=False).head(10)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Loading file"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "metadata": {},
   "outputs": [],
   "source": [
    "dely = pd.read_csv('Desktop\\deliveries.csv')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>match_id</th>\n",
       "      <th>inning</th>\n",
       "      <th>batting_team</th>\n",
       "      <th>bowling_team</th>\n",
       "      <th>over</th>\n",
       "      <th>ball</th>\n",
       "      <th>batsman</th>\n",
       "      <th>non_striker</th>\n",
       "      <th>bowler</th>\n",
       "      <th>is_super_over</th>\n",
       "      <th>...</th>\n",
       "      <th>bye_runs</th>\n",
       "      <th>legbye_runs</th>\n",
       "      <th>noball_runs</th>\n",
       "      <th>penalty_runs</th>\n",
       "      <th>batsman_runs</th>\n",
       "      <th>extra_runs</th>\n",
       "      <th>total_runs</th>\n",
       "      <th>player_dismissed</th>\n",
       "      <th>dismissal_kind</th>\n",
       "      <th>fielder</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>Sunrisers Hyderabad</td>\n",
       "      <td>Royal Challengers Bangalore</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>DA Warner</td>\n",
       "      <td>S Dhawan</td>\n",
       "      <td>TS Mills</td>\n",
       "      <td>0</td>\n",
       "      <td>...</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>Sunrisers Hyderabad</td>\n",
       "      <td>Royal Challengers Bangalore</td>\n",
       "      <td>1</td>\n",
       "      <td>2</td>\n",
       "      <td>DA Warner</td>\n",
       "      <td>S Dhawan</td>\n",
       "      <td>TS Mills</td>\n",
       "      <td>0</td>\n",
       "      <td>...</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>Sunrisers Hyderabad</td>\n",
       "      <td>Royal Challengers Bangalore</td>\n",
       "      <td>1</td>\n",
       "      <td>3</td>\n",
       "      <td>DA Warner</td>\n",
       "      <td>S Dhawan</td>\n",
       "      <td>TS Mills</td>\n",
       "      <td>0</td>\n",
       "      <td>...</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>4</td>\n",
       "      <td>0</td>\n",
       "      <td>4</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>Sunrisers Hyderabad</td>\n",
       "      <td>Royal Challengers Bangalore</td>\n",
       "      <td>1</td>\n",
       "      <td>4</td>\n",
       "      <td>DA Warner</td>\n",
       "      <td>S Dhawan</td>\n",
       "      <td>TS Mills</td>\n",
       "      <td>0</td>\n",
       "      <td>...</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>Sunrisers Hyderabad</td>\n",
       "      <td>Royal Challengers Bangalore</td>\n",
       "      <td>1</td>\n",
       "      <td>5</td>\n",
       "      <td>DA Warner</td>\n",
       "      <td>S Dhawan</td>\n",
       "      <td>TS Mills</td>\n",
       "      <td>0</td>\n",
       "      <td>...</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>2</td>\n",
       "      <td>2</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>5 rows × 21 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "   match_id  inning         batting_team                 bowling_team  over  \\\n",
       "0         1       1  Sunrisers Hyderabad  Royal Challengers Bangalore     1   \n",
       "1         1       1  Sunrisers Hyderabad  Royal Challengers Bangalore     1   \n",
       "2         1       1  Sunrisers Hyderabad  Royal Challengers Bangalore     1   \n",
       "3         1       1  Sunrisers Hyderabad  Royal Challengers Bangalore     1   \n",
       "4         1       1  Sunrisers Hyderabad  Royal Challengers Bangalore     1   \n",
       "\n",
       "   ball    batsman non_striker    bowler  is_super_over  ...  bye_runs  \\\n",
       "0     1  DA Warner    S Dhawan  TS Mills              0  ...         0   \n",
       "1     2  DA Warner    S Dhawan  TS Mills              0  ...         0   \n",
       "2     3  DA Warner    S Dhawan  TS Mills              0  ...         0   \n",
       "3     4  DA Warner    S Dhawan  TS Mills              0  ...         0   \n",
       "4     5  DA Warner    S Dhawan  TS Mills              0  ...         0   \n",
       "\n",
       "   legbye_runs  noball_runs  penalty_runs  batsman_runs  extra_runs  \\\n",
       "0            0            0             0             0           0   \n",
       "1            0            0             0             0           0   \n",
       "2            0            0             0             4           0   \n",
       "3            0            0             0             0           0   \n",
       "4            0            0             0             0           2   \n",
       "\n",
       "   total_runs  player_dismissed dismissal_kind fielder  \n",
       "0           0               NaN            NaN     NaN  \n",
       "1           0               NaN            NaN     NaN  \n",
       "2           4               NaN            NaN     NaN  \n",
       "3           0               NaN            NaN     NaN  \n",
       "4           2               NaN            NaN     NaN  \n",
       "\n",
       "[5 rows x 21 columns]"
      ]
     },
     "execution_count": 31,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "dely.head()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Top Run scorers"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 329,
   "metadata": {},
   "outputs": [],
   "source": [
    "delys=dely.groupby(['batsman'])['match_id'].nunique()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 330,
   "metadata": {},
   "outputs": [],
   "source": [
    "delysort= dely['batsman_runs'].groupby(dely['batsman']).sum()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 331,
   "metadata": {},
   "outputs": [],
   "source": [
    "ds=pd.merge(delys,delysort,on='batsman')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 333,
   "metadata": {},
   "outputs": [],
   "source": [
    "dss=ds.sort_values(by='batsman_runs',ascending=False)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 338,
   "metadata": {},
   "outputs": [],
   "source": [
    "dss.columns = ['Matches','Runs']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 339,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Matches</th>\n",
       "      <th>Runs</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>batsman</th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>V Kohli</th>\n",
       "      <td>169</td>\n",
       "      <td>5434</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>SK Raina</th>\n",
       "      <td>189</td>\n",
       "      <td>5415</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>RG Sharma</th>\n",
       "      <td>182</td>\n",
       "      <td>4914</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>DA Warner</th>\n",
       "      <td>126</td>\n",
       "      <td>4741</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>S Dhawan</th>\n",
       "      <td>158</td>\n",
       "      <td>4632</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>CH Gayle</th>\n",
       "      <td>124</td>\n",
       "      <td>4560</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>MS Dhoni</th>\n",
       "      <td>170</td>\n",
       "      <td>4477</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>RV Uthappa</th>\n",
       "      <td>170</td>\n",
       "      <td>4446</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>AB de Villiers</th>\n",
       "      <td>142</td>\n",
       "      <td>4428</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>G Gambhir</th>\n",
       "      <td>151</td>\n",
       "      <td>4223</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                Matches  Runs\n",
       "batsman                      \n",
       "V Kohli             169  5434\n",
       "SK Raina            189  5415\n",
       "RG Sharma           182  4914\n",
       "DA Warner           126  4741\n",
       "S Dhawan            158  4632\n",
       "CH Gayle            124  4560\n",
       "MS Dhoni            170  4477\n",
       "RV Uthappa          170  4446\n",
       "AB de Villiers      142  4428\n",
       "G Gambhir           151  4223"
      ]
     },
     "execution_count": 339,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "dss.head(10)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Players with most no. of matches played"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "metadata": {},
   "outputs": [],
   "source": [
    "delm=dely['match_id'].groupby(dely['batsman']).nunique()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "batsman\n",
       "SK Raina          189\n",
       "RG Sharma         182\n",
       "RV Uthappa        170\n",
       "MS Dhoni          170\n",
       "V Kohli           169\n",
       "KD Karthik        162\n",
       "S Dhawan          158\n",
       "YK Pathan         153\n",
       "G Gambhir         151\n",
       "AB de Villiers    142\n",
       "Name: match_id, dtype: int64"
      ]
     },
     "execution_count": 35,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "delm.sort_values(ascending=False).head(10)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Highest wicket takers"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "metadata": {},
   "outputs": [],
   "source": [
    "m2=dely.dropna()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 37,
   "metadata": {},
   "outputs": [],
   "source": [
    "m12=m2[m2['dismissal_kind']!= 'run out']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 38,
   "metadata": {},
   "outputs": [],
   "source": [
    "m123=m12['player_dismissed'].groupby(m12['bowler']).count()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 39,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "bowler\n",
       "A Mishra           114\n",
       "DJ Bravo           113\n",
       "Harbhajan Singh    101\n",
       "SL Malinga          91\n",
       "UT Yadav            89\n",
       "PP Chawla           86\n",
       "R Ashwin            86\n",
       "B Kumar             85\n",
       "R Vinay Kumar       82\n",
       "A Nehra             76\n",
       "Name: player_dismissed, dtype: int64"
      ]
     },
     "execution_count": 39,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "m123.sort_values(ascending=False).head(10)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Most no. of stumpings"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 40,
   "metadata": {},
   "outputs": [],
   "source": [
    "m1234=m12[m12['dismissal_kind']=='stumped']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 41,
   "metadata": {},
   "outputs": [],
   "source": [
    "kula=m1234['player_dismissed'].groupby(m1234['fielder']).count()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 42,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "fielder\n",
       "MS Dhoni         38\n",
       "RV Uthappa       32\n",
       "KD Karthik       29\n",
       "WP Saha          18\n",
       "AC Gilchrist     16\n",
       "PA Patel         16\n",
       "NV Ojha          10\n",
       "KC Sangakkara     9\n",
       "RR Pant           9\n",
       "Q de Kock         8\n",
       "Name: player_dismissed, dtype: int64"
      ]
     },
     "execution_count": 42,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "kula.sort_values(ascending=False).head(10)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# No. of matches played"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 348,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "756"
      ]
     },
     "execution_count": 348,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data['id'].count()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# No. of times a team won when it didn't win the toss"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 44,
   "metadata": {},
   "outputs": [],
   "source": [
    "d1=data[data['toss_winner']!=data['winner']]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 45,
   "metadata": {},
   "outputs": [],
   "source": [
    "d12=d1['winner'].groupby(d1['winner']).count()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 46,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "winner\n",
       "Mumbai Indians                 53\n",
       "Kings XI Punjab                47\n",
       "Royal Challengers Bangalore    43\n",
       "Chennai Super Kings            43\n",
       "Kolkata Knight Riders          39\n",
       "Sunrisers Hyderabad            35\n",
       "Rajasthan Royals               33\n",
       "Delhi Daredevils               32\n",
       "Deccan Chargers                10\n",
       "Pune Warriors                   9\n",
       "Rising Pune Supergiant          5\n",
       "Gujarat Lions                   3\n",
       "Delhi Capitals                  3\n",
       "Rising Pune Supergiants         2\n",
       "Kochi Tuskers Kerala            2\n",
       "Name: winner, dtype: int64"
      ]
     },
     "execution_count": 46,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "d12.sort_values(ascending=False)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Most extra runs conceded by a bowler"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 47,
   "metadata": {},
   "outputs": [],
   "source": [
    "delyy=dely['extra_runs'].groupby(dely['bowler']).sum()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 48,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "bowler\n",
       "SL Malinga         293\n",
       "P Kumar            236\n",
       "UT Yadav           219\n",
       "DJ Bravo           201\n",
       "B Kumar            197\n",
       "I Sharma           194\n",
       "RP Singh           181\n",
       "SR Watson          171\n",
       "DW Steyn           171\n",
       "Harbhajan Singh    170\n",
       "Name: extra_runs, dtype: int64"
      ]
     },
     "execution_count": 48,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "delyy.sort_values(ascending=False).head(10)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# No of times the toss winner chose to field"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 349,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "463"
      ]
     },
     "execution_count": 349,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "d1=data[data['toss_decision']=='field']\n",
    "d1['toss_decision'].count()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# No. of times the toss winner chose to field & won the match"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 352,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "259"
      ]
     },
     "execution_count": 352,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "d1[d1['toss_winner']==d1['winner']]['id'].count()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# No. of times toss winner chose to bat"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 51,
   "metadata": {},
   "outputs": [],
   "source": [
    "d2=data[data['toss_decision']=='bat']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 353,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "293"
      ]
     },
     "execution_count": 353,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "d2['toss_winner'].count()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# No. of times toss winner chose to bat and won the match"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 354,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "134"
      ]
     },
     "execution_count": 354,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "d2[d2['toss_winner']==d2['winner']]['id'].count()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# No. of big margin wins(30 runs) by a team batting first"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 54,
   "metadata": {},
   "outputs": [],
   "source": [
    "dat1=data[data['win_by_runs']!=0]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 55,
   "metadata": {},
   "outputs": [],
   "source": [
    "dat12=dat1[dat1['win_by_runs']>=30]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 56,
   "metadata": {},
   "outputs": [],
   "source": [
    "dat123=dat12['win_by_runs'].groupby(dat12['winner']).count()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 57,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "winner\n",
       "Mumbai Indians                 24\n",
       "Chennai Super Kings            22\n",
       "Kolkata Knight Riders          15\n",
       "Royal Challengers Bangalore    13\n",
       "Rajasthan Royals               13\n",
       "Delhi Daredevils               10\n",
       "Kings XI Punjab                 9\n",
       "Sunrisers Hyderabad             8\n",
       "Deccan Chargers                 5\n",
       "Delhi Capitals                  2\n",
       "Rising Pune Supergiants         1\n",
       "Rising Pune Supergiant          1\n",
       "Pune Warriors                   1\n",
       "Name: win_by_runs, dtype: int64"
      ]
     },
     "execution_count": 57,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "dat123.sort_values(ascending=False)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# No. of big margin wins ( >4 wickets) by a team bowling first"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 58,
   "metadata": {},
   "outputs": [],
   "source": [
    "dat4=data[data['win_by_wickets']!=0]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 59,
   "metadata": {},
   "outputs": [],
   "source": [
    "dat45=dat4[dat4['win_by_wickets']>=4]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 60,
   "metadata": {},
   "outputs": [],
   "source": [
    "dat456=dat45['win_by_wickets'].groupby(dat45['winner']).count()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 61,
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "winner\n",
       "Kolkata Knight Riders          52\n",
       "Mumbai Indians                 48\n",
       "Royal Challengers Bangalore    45\n",
       "Chennai Super Kings            45\n",
       "Kings XI Punjab                41\n",
       "Delhi Daredevils               40\n",
       "Rajasthan Royals               39\n",
       "Sunrisers Hyderabad            25\n",
       "Deccan Chargers                11\n",
       "Gujarat Lions                  10\n",
       "Pune Warriors                   6\n",
       "Rising Pune Supergiant          5\n",
       "Delhi Capitals                  5\n",
       "Kochi Tuskers Kerala            4\n",
       "Rising Pune Supergiants         3\n",
       "Name: win_by_wickets, dtype: int64"
      ]
     },
     "execution_count": 61,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "dat456.sort_values(ascending = False)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Most no. of catches"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 62,
   "metadata": {
    "collapsed": true
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>match_id</th>\n",
       "      <th>inning</th>\n",
       "      <th>batting_team</th>\n",
       "      <th>bowling_team</th>\n",
       "      <th>over</th>\n",
       "      <th>ball</th>\n",
       "      <th>batsman</th>\n",
       "      <th>non_striker</th>\n",
       "      <th>bowler</th>\n",
       "      <th>is_super_over</th>\n",
       "      <th>...</th>\n",
       "      <th>bye_runs</th>\n",
       "      <th>legbye_runs</th>\n",
       "      <th>noball_runs</th>\n",
       "      <th>penalty_runs</th>\n",
       "      <th>batsman_runs</th>\n",
       "      <th>extra_runs</th>\n",
       "      <th>total_runs</th>\n",
       "      <th>player_dismissed</th>\n",
       "      <th>dismissal_kind</th>\n",
       "      <th>fielder</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>11</th>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>Sunrisers Hyderabad</td>\n",
       "      <td>Royal Challengers Bangalore</td>\n",
       "      <td>2</td>\n",
       "      <td>5</td>\n",
       "      <td>DA Warner</td>\n",
       "      <td>S Dhawan</td>\n",
       "      <td>A Choudhary</td>\n",
       "      <td>0</td>\n",
       "      <td>...</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>DA Warner</td>\n",
       "      <td>caught</td>\n",
       "      <td>Mandeep Singh</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>64</th>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>Sunrisers Hyderabad</td>\n",
       "      <td>Royal Challengers Bangalore</td>\n",
       "      <td>11</td>\n",
       "      <td>3</td>\n",
       "      <td>S Dhawan</td>\n",
       "      <td>MC Henriques</td>\n",
       "      <td>STR Binny</td>\n",
       "      <td>0</td>\n",
       "      <td>...</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>S Dhawan</td>\n",
       "      <td>caught</td>\n",
       "      <td>Sachin Baby</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>94</th>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>Sunrisers Hyderabad</td>\n",
       "      <td>Royal Challengers Bangalore</td>\n",
       "      <td>16</td>\n",
       "      <td>2</td>\n",
       "      <td>MC Henriques</td>\n",
       "      <td>Yuvraj Singh</td>\n",
       "      <td>YS Chahal</td>\n",
       "      <td>0</td>\n",
       "      <td>...</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>MC Henriques</td>\n",
       "      <td>caught</td>\n",
       "      <td>Sachin Baby</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>165</th>\n",
       "      <td>1</td>\n",
       "      <td>2</td>\n",
       "      <td>Royal Challengers Bangalore</td>\n",
       "      <td>Sunrisers Hyderabad</td>\n",
       "      <td>7</td>\n",
       "      <td>3</td>\n",
       "      <td>CH Gayle</td>\n",
       "      <td>TM Head</td>\n",
       "      <td>DJ Hooda</td>\n",
       "      <td>0</td>\n",
       "      <td>...</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>CH Gayle</td>\n",
       "      <td>caught</td>\n",
       "      <td>DA Warner</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>199</th>\n",
       "      <td>1</td>\n",
       "      <td>2</td>\n",
       "      <td>Royal Challengers Bangalore</td>\n",
       "      <td>Sunrisers Hyderabad</td>\n",
       "      <td>12</td>\n",
       "      <td>4</td>\n",
       "      <td>KM Jadhav</td>\n",
       "      <td>TM Head</td>\n",
       "      <td>MC Henriques</td>\n",
       "      <td>0</td>\n",
       "      <td>...</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>KM Jadhav</td>\n",
       "      <td>run out</td>\n",
       "      <td>BCJ Cutting</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>...</th>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>178977</th>\n",
       "      <td>11415</td>\n",
       "      <td>2</td>\n",
       "      <td>Chennai Super Kings</td>\n",
       "      <td>Mumbai Indians</td>\n",
       "      <td>4</td>\n",
       "      <td>6</td>\n",
       "      <td>F du Plessis</td>\n",
       "      <td>SR Watson</td>\n",
       "      <td>KH Pandya</td>\n",
       "      <td>0</td>\n",
       "      <td>...</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>F du Plessis</td>\n",
       "      <td>stumped</td>\n",
       "      <td>Q de Kock</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>179019</th>\n",
       "      <td>11415</td>\n",
       "      <td>2</td>\n",
       "      <td>Chennai Super Kings</td>\n",
       "      <td>Mumbai Indians</td>\n",
       "      <td>11</td>\n",
       "      <td>3</td>\n",
       "      <td>AT Rayudu</td>\n",
       "      <td>SR Watson</td>\n",
       "      <td>JJ Bumrah</td>\n",
       "      <td>0</td>\n",
       "      <td>...</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>AT Rayudu</td>\n",
       "      <td>caught</td>\n",
       "      <td>Q de Kock</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>179033</th>\n",
       "      <td>11415</td>\n",
       "      <td>2</td>\n",
       "      <td>Chennai Super Kings</td>\n",
       "      <td>Mumbai Indians</td>\n",
       "      <td>13</td>\n",
       "      <td>5</td>\n",
       "      <td>SR Watson</td>\n",
       "      <td>MS Dhoni</td>\n",
       "      <td>HH Pandya</td>\n",
       "      <td>0</td>\n",
       "      <td>...</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>MS Dhoni</td>\n",
       "      <td>run out</td>\n",
       "      <td>Ishan Kishan</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>179067</th>\n",
       "      <td>11415</td>\n",
       "      <td>2</td>\n",
       "      <td>Chennai Super Kings</td>\n",
       "      <td>Mumbai Indians</td>\n",
       "      <td>19</td>\n",
       "      <td>2</td>\n",
       "      <td>DJ Bravo</td>\n",
       "      <td>SR Watson</td>\n",
       "      <td>JJ Bumrah</td>\n",
       "      <td>0</td>\n",
       "      <td>...</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>DJ Bravo</td>\n",
       "      <td>caught</td>\n",
       "      <td>Q de Kock</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>179075</th>\n",
       "      <td>11415</td>\n",
       "      <td>2</td>\n",
       "      <td>Chennai Super Kings</td>\n",
       "      <td>Mumbai Indians</td>\n",
       "      <td>20</td>\n",
       "      <td>4</td>\n",
       "      <td>SR Watson</td>\n",
       "      <td>RA Jadeja</td>\n",
       "      <td>SL Malinga</td>\n",
       "      <td>0</td>\n",
       "      <td>...</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>SR Watson</td>\n",
       "      <td>run out</td>\n",
       "      <td>KH Pandya</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>6448 rows × 21 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "        match_id  inning                 batting_team  \\\n",
       "11             1       1          Sunrisers Hyderabad   \n",
       "64             1       1          Sunrisers Hyderabad   \n",
       "94             1       1          Sunrisers Hyderabad   \n",
       "165            1       2  Royal Challengers Bangalore   \n",
       "199            1       2  Royal Challengers Bangalore   \n",
       "...          ...     ...                          ...   \n",
       "178977     11415       2          Chennai Super Kings   \n",
       "179019     11415       2          Chennai Super Kings   \n",
       "179033     11415       2          Chennai Super Kings   \n",
       "179067     11415       2          Chennai Super Kings   \n",
       "179075     11415       2          Chennai Super Kings   \n",
       "\n",
       "                       bowling_team  over  ball       batsman   non_striker  \\\n",
       "11      Royal Challengers Bangalore     2     5     DA Warner      S Dhawan   \n",
       "64      Royal Challengers Bangalore    11     3      S Dhawan  MC Henriques   \n",
       "94      Royal Challengers Bangalore    16     2  MC Henriques  Yuvraj Singh   \n",
       "165             Sunrisers Hyderabad     7     3      CH Gayle       TM Head   \n",
       "199             Sunrisers Hyderabad    12     4     KM Jadhav       TM Head   \n",
       "...                             ...   ...   ...           ...           ...   \n",
       "178977               Mumbai Indians     4     6  F du Plessis     SR Watson   \n",
       "179019               Mumbai Indians    11     3     AT Rayudu     SR Watson   \n",
       "179033               Mumbai Indians    13     5     SR Watson      MS Dhoni   \n",
       "179067               Mumbai Indians    19     2      DJ Bravo     SR Watson   \n",
       "179075               Mumbai Indians    20     4     SR Watson     RA Jadeja   \n",
       "\n",
       "              bowler  is_super_over  ...  bye_runs  legbye_runs  noball_runs  \\\n",
       "11       A Choudhary              0  ...         0            0            0   \n",
       "64         STR Binny              0  ...         0            0            0   \n",
       "94         YS Chahal              0  ...         0            0            0   \n",
       "165         DJ Hooda              0  ...         0            0            0   \n",
       "199     MC Henriques              0  ...         0            0            0   \n",
       "...              ...            ...  ...       ...          ...          ...   \n",
       "178977     KH Pandya              0  ...         0            0            0   \n",
       "179019     JJ Bumrah              0  ...         0            0            0   \n",
       "179033     HH Pandya              0  ...         0            0            0   \n",
       "179067     JJ Bumrah              0  ...         0            0            0   \n",
       "179075    SL Malinga              0  ...         0            0            0   \n",
       "\n",
       "        penalty_runs  batsman_runs  extra_runs  total_runs  player_dismissed  \\\n",
       "11                 0             0           0           0         DA Warner   \n",
       "64                 0             0           0           0          S Dhawan   \n",
       "94                 0             0           0           0      MC Henriques   \n",
       "165                0             0           0           0          CH Gayle   \n",
       "199                0             1           0           1         KM Jadhav   \n",
       "...              ...           ...         ...         ...               ...   \n",
       "178977             0             0           0           0      F du Plessis   \n",
       "179019             0             0           0           0         AT Rayudu   \n",
       "179033             0             1           0           1          MS Dhoni   \n",
       "179067             0             0           0           0          DJ Bravo   \n",
       "179075             0             1           0           1         SR Watson   \n",
       "\n",
       "       dismissal_kind        fielder  \n",
       "11             caught  Mandeep Singh  \n",
       "64             caught    Sachin Baby  \n",
       "94             caught    Sachin Baby  \n",
       "165            caught      DA Warner  \n",
       "199           run out    BCJ Cutting  \n",
       "...               ...            ...  \n",
       "178977        stumped      Q de Kock  \n",
       "179019         caught      Q de Kock  \n",
       "179033        run out   Ishan Kishan  \n",
       "179067         caught      Q de Kock  \n",
       "179075        run out      KH Pandya  \n",
       "\n",
       "[6448 rows x 21 columns]"
      ]
     },
     "execution_count": 62,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "m2"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 63,
   "metadata": {},
   "outputs": [],
   "source": [
    "m3=m2[m2['dismissal_kind']=='caught']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 74,
   "metadata": {},
   "outputs": [],
   "source": [
    "m4=m3.groupby(m3['fielder'])['fielder'].count()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 73,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "fielder\n",
       "KD Karthik        109\n",
       "SK Raina           99\n",
       "MS Dhoni           98\n",
       "AB de Villiers     93\n",
       "RV Uthappa         84\n",
       "RG Sharma          82\n",
       "KA Pollard         76\n",
       "V Kohli            73\n",
       "PA Patel           69\n",
       "S Dhawan           68\n",
       "Name: fielder, dtype: int64"
      ]
     },
     "execution_count": 73,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "m4.sort_values(ascending=False).head(10)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Matches where dl was applied"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 78,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "19"
      ]
     },
     "execution_count": 78,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data[data['dl_applied']!=0]['id'].count()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Bowlers conceding most no balls & penalties"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 88,
   "metadata": {},
   "outputs": [],
   "source": [
    "dely['exr']=dely['noball_runs']+dely['penalty_runs']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 91,
   "metadata": {},
   "outputs": [],
   "source": [
    "y1=dely['exr'].groupby(dely['bowler']).sum()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 93,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "bowler\n",
       "S Sreesanth    27\n",
       "SL Malinga     25\n",
       "JJ Bumrah      23\n",
       "I Sharma       21\n",
       "A Mishra       20\n",
       "UT Yadav       19\n",
       "JA Morkel      18\n",
       "AB Dinda       14\n",
       "SW Tait        14\n",
       "SR Watson      13\n",
       "Name: exr, dtype: int64"
      ]
     },
     "execution_count": 93,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "y1.sort_values(ascending=False).head(10)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# No. of matches where match is a tie & super over was played"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 97,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "7"
      ]
     },
     "execution_count": 97,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "dely[dely['is_super_over']!=0]['match_id'].nunique()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 110,
   "metadata": {},
   "outputs": [],
   "source": [
    "d10=dely[dely['dismissal_kind']=='run out']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 115,
   "metadata": {},
   "outputs": [],
   "source": [
    "d11= d10['fielder'].groupby(d10['fielder']).count()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Most runouts"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 116,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "fielder\n",
       "MS Dhoni          23\n",
       "RA Jadeja         20\n",
       "V Kohli           17\n",
       "SK Raina          16\n",
       "MK Pandey         14\n",
       "AB de Villiers    14\n",
       "KD Karthik        14\n",
       "DJ Bravo          12\n",
       "PA Patel          12\n",
       "YK Pathan         10\n",
       "Name: fielder, dtype: int64"
      ]
     },
     "execution_count": 116,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "d11.sort_values(ascending=False).head(10)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Best strike rate"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 128,
   "metadata": {},
   "outputs": [],
   "source": [
    "d7=dely.groupby(dely['batsman'])['ball'].count()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 129,
   "metadata": {},
   "outputs": [],
   "source": [
    "d8=dely.groupby(dely['batsman'])['batsman_runs'].sum()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 189,
   "metadata": {},
   "outputs": [],
   "source": [
    "d9=pd.merge(d7,d8, on = 'batsman')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 190,
   "metadata": {},
   "outputs": [],
   "source": [
    "d9['strike_rate']=round(d9['batsman_runs']*100/d9['ball'],2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 191,
   "metadata": {},
   "outputs": [],
   "source": [
    "d10=d9.sort_values(by='strike_rate',ascending=False)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# batsman playing <500 balls not to be considered in top strike rated players as it is not enough to judge"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 192,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>ball</th>\n",
       "      <th>batsman_runs</th>\n",
       "      <th>strike_rate</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>batsman</th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>AD Russell</th>\n",
       "      <td>803</td>\n",
       "      <td>1445</td>\n",
       "      <td>179.95</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>RR Pant</th>\n",
       "      <td>1104</td>\n",
       "      <td>1792</td>\n",
       "      <td>162.32</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>GJ Maxwell</th>\n",
       "      <td>902</td>\n",
       "      <td>1403</td>\n",
       "      <td>155.54</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>HH Pandya</th>\n",
       "      <td>736</td>\n",
       "      <td>1118</td>\n",
       "      <td>151.90</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>JC Buttler</th>\n",
       "      <td>954</td>\n",
       "      <td>1431</td>\n",
       "      <td>150.00</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>V Sehwag</th>\n",
       "      <td>1833</td>\n",
       "      <td>2728</td>\n",
       "      <td>148.83</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>AB de Villiers</th>\n",
       "      <td>2977</td>\n",
       "      <td>4428</td>\n",
       "      <td>148.74</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>CH Gayle</th>\n",
       "      <td>3131</td>\n",
       "      <td>4560</td>\n",
       "      <td>145.64</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>KH Pandya</th>\n",
       "      <td>635</td>\n",
       "      <td>915</td>\n",
       "      <td>144.09</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>KA Pollard</th>\n",
       "      <td>1964</td>\n",
       "      <td>2784</td>\n",
       "      <td>141.75</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                ball  batsman_runs  strike_rate\n",
       "batsman                                        \n",
       "AD Russell       803          1445       179.95\n",
       "RR Pant         1104          1792       162.32\n",
       "GJ Maxwell       902          1403       155.54\n",
       "HH Pandya        736          1118       151.90\n",
       "JC Buttler       954          1431       150.00\n",
       "V Sehwag        1833          2728       148.83\n",
       "AB de Villiers  2977          4428       148.74\n",
       "CH Gayle        3131          4560       145.64\n",
       "KH Pandya        635           915       144.09\n",
       "KA Pollard      1964          2784       141.75"
      ]
     },
     "execution_count": 192,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "d10[d10['ball']>=500].head(10)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Most economical bowlers ( per over )"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 162,
   "metadata": {},
   "outputs": [],
   "source": [
    "e9=dely.groupby(dely['bowler'])['total_runs'].sum()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 169,
   "metadata": {},
   "outputs": [],
   "source": [
    "e10=dely.groupby(dely['bowler'])['ball'].count()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 197,
   "metadata": {},
   "outputs": [],
   "source": [
    "e11=pd.merge(e9,e10 , on='bowler')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 201,
   "metadata": {},
   "outputs": [],
   "source": [
    "e11['economy']=round(e11['total_runs']*6/e11['ball'],2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 321,
   "metadata": {},
   "outputs": [],
   "source": [
    "e12=e11[e11['ball']>=72]\n",
    "e12.columns = ['total_runs','no. of balls','economy']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 322,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>total_runs</th>\n",
       "      <th>no. of balls</th>\n",
       "      <th>economy</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>bowler</th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>Sohail Tanvir</th>\n",
       "      <td>275</td>\n",
       "      <td>265</td>\n",
       "      <td>6.23</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>A Chandila</th>\n",
       "      <td>245</td>\n",
       "      <td>234</td>\n",
       "      <td>6.28</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>FH Edwards</th>\n",
       "      <td>160</td>\n",
       "      <td>150</td>\n",
       "      <td>6.40</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>L Ngidi</th>\n",
       "      <td>175</td>\n",
       "      <td>163</td>\n",
       "      <td>6.44</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>SMSM Senanayake</th>\n",
       "      <td>211</td>\n",
       "      <td>195</td>\n",
       "      <td>6.49</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>J Yadav</th>\n",
       "      <td>248</td>\n",
       "      <td>226</td>\n",
       "      <td>6.58</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>SM Pollock</th>\n",
       "      <td>307</td>\n",
       "      <td>280</td>\n",
       "      <td>6.58</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>LH Ferguson</th>\n",
       "      <td>96</td>\n",
       "      <td>87</td>\n",
       "      <td>6.62</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>A Kumble</th>\n",
       "      <td>1089</td>\n",
       "      <td>983</td>\n",
       "      <td>6.65</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>GD McGrath</th>\n",
       "      <td>366</td>\n",
       "      <td>329</td>\n",
       "      <td>6.67</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                 total_runs  no. of balls  economy\n",
       "bowler                                            \n",
       "Sohail Tanvir           275           265     6.23\n",
       "A Chandila              245           234     6.28\n",
       "FH Edwards              160           150     6.40\n",
       "L Ngidi                 175           163     6.44\n",
       "SMSM Senanayake         211           195     6.49\n",
       "J Yadav                 248           226     6.58\n",
       "SM Pollock              307           280     6.58\n",
       "LH Ferguson              96            87     6.62\n",
       "A Kumble               1089           983     6.65\n",
       "GD McGrath              366           329     6.67"
      ]
     },
     "execution_count": 322,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "e12.sort_values(by='economy',ascending=True).head(10)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Most no. of sixes"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 182,
   "metadata": {},
   "outputs": [],
   "source": [
    "dely1=dely[dely['batsman_runs']==6]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 183,
   "metadata": {},
   "outputs": [],
   "source": [
    "dely12=dely1.groupby(dely1['batsman'])['batsman_runs'].count()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 184,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "batsman\n",
       "CH Gayle          327\n",
       "AB de Villiers    214\n",
       "MS Dhoni          207\n",
       "SK Raina          195\n",
       "RG Sharma         194\n",
       "V Kohli           191\n",
       "DA Warner         181\n",
       "SR Watson         177\n",
       "KA Pollard        175\n",
       "YK Pathan         161\n",
       "Name: batsman_runs, dtype: int64"
      ]
     },
     "execution_count": 184,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "dely12.sort_values(ascending=False).head(10)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Best Average"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 311,
   "metadata": {},
   "outputs": [],
   "source": [
    "f1=dely.groupby(dely['batsman'])['match_id'].nunique()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 312,
   "metadata": {},
   "outputs": [],
   "source": [
    "f2=dely.groupby(dely['batsman'])['batsman_runs'].sum()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 313,
   "metadata": {},
   "outputs": [],
   "source": [
    "f3=pd.merge(f1,f2,on='batsman')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 315,
   "metadata": {},
   "outputs": [],
   "source": [
    "f3['average']=round(f3['batsman_runs']/f3['match_id'],2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 316,
   "metadata": {},
   "outputs": [],
   "source": [
    "f4=f3.sort_values(by='average',ascending=False)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 318,
   "metadata": {},
   "outputs": [],
   "source": [
    "f4.columns = ['no. of matches','total runs','average']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 320,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>no. of matches</th>\n",
       "      <th>total runs</th>\n",
       "      <th>average</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>batsman</th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>DA Warner</th>\n",
       "      <td>126</td>\n",
       "      <td>4741</td>\n",
       "      <td>37.63</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>LMP Simmons</th>\n",
       "      <td>29</td>\n",
       "      <td>1079</td>\n",
       "      <td>37.21</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>CH Gayle</th>\n",
       "      <td>124</td>\n",
       "      <td>4560</td>\n",
       "      <td>36.77</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>SE Marsh</th>\n",
       "      <td>69</td>\n",
       "      <td>2489</td>\n",
       "      <td>36.07</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>KL Rahul</th>\n",
       "      <td>58</td>\n",
       "      <td>2013</td>\n",
       "      <td>34.71</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>ML Hayden</th>\n",
       "      <td>32</td>\n",
       "      <td>1107</td>\n",
       "      <td>34.59</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>MEK Hussey</th>\n",
       "      <td>58</td>\n",
       "      <td>1977</td>\n",
       "      <td>34.09</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>RR Pant</th>\n",
       "      <td>54</td>\n",
       "      <td>1792</td>\n",
       "      <td>33.19</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>KS Williamson</th>\n",
       "      <td>41</td>\n",
       "      <td>1319</td>\n",
       "      <td>32.17</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>V Kohli</th>\n",
       "      <td>169</td>\n",
       "      <td>5434</td>\n",
       "      <td>32.15</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "               no. of matches  total runs  average\n",
       "batsman                                           \n",
       "DA Warner                 126        4741    37.63\n",
       "LMP Simmons                29        1079    37.21\n",
       "CH Gayle                  124        4560    36.77\n",
       "SE Marsh                   69        2489    36.07\n",
       "KL Rahul                   58        2013    34.71\n",
       "ML Hayden                  32        1107    34.59\n",
       "MEK Hussey                 58        1977    34.09\n",
       "RR Pant                    54        1792    33.19\n",
       "KS Williamson              41        1319    32.17\n",
       "V Kohli                   169        5434    32.15"
      ]
     },
     "execution_count": 320,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "f4[f4['no. of matches']>=20].head(10)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Caught & bowled"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 303,
   "metadata": {},
   "outputs": [],
   "source": [
    "d=dely[dely['bowler']==dely['fielder']]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 304,
   "metadata": {},
   "outputs": [],
   "source": [
    "d1=d[d['dismissal_kind']!='run out']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 323,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "bowler\n",
       "S Gopal           5\n",
       "Kuldeep Yadav     5\n",
       "Imran Tahir       3\n",
       "RA Jadeja         2\n",
       "Sandeep Sharma    2\n",
       "Name: bowler, dtype: int64"
      ]
     },
     "execution_count": 323,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "d11=d1.groupby(d1['bowler'])['bowler'].count()\n",
    "d11.sort_values(ascending=False).head()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Average score of a team in an innings"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 340,
   "metadata": {},
   "outputs": [],
   "source": [
    "av=dely.groupby(dely['batting_team'])['match_id'].nunique()\n",
    "av1=dely.groupby(dely['batting_team'])['total_runs'].sum()\n",
    "a=pd.merge(av,av1,on='batting_team')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 347,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Matches</th>\n",
       "      <th>Team avg score</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>batting_team</th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>Delhi Capitals</th>\n",
       "      <td>16</td>\n",
       "      <td>164.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Gujarat Lions</th>\n",
       "      <td>30</td>\n",
       "      <td>162.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Chennai Super Kings</th>\n",
       "      <td>164</td>\n",
       "      <td>161.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Mumbai Indians</th>\n",
       "      <td>187</td>\n",
       "      <td>159.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Kings XI Punjab</th>\n",
       "      <td>176</td>\n",
       "      <td>158.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Sunrisers Hyderabad</th>\n",
       "      <td>108</td>\n",
       "      <td>158.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Royal Challengers Bangalore</th>\n",
       "      <td>180</td>\n",
       "      <td>156.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Kolkata Knight Riders</th>\n",
       "      <td>178</td>\n",
       "      <td>154.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Rajasthan Royals</th>\n",
       "      <td>146</td>\n",
       "      <td>154.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Rising Pune Supergiant</th>\n",
       "      <td>16</td>\n",
       "      <td>154.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Deccan Chargers</th>\n",
       "      <td>75</td>\n",
       "      <td>153.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Delhi Daredevils</th>\n",
       "      <td>161</td>\n",
       "      <td>151.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Rising Pune Supergiants</th>\n",
       "      <td>14</td>\n",
       "      <td>147.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Pune Warriors</th>\n",
       "      <td>45</td>\n",
       "      <td>141.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Kochi Tuskers Kerala</th>\n",
       "      <td>14</td>\n",
       "      <td>136.0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                             Matches  Team avg score\n",
       "batting_team                                        \n",
       "Delhi Capitals                    16           164.0\n",
       "Gujarat Lions                     30           162.0\n",
       "Chennai Super Kings              164           161.0\n",
       "Mumbai Indians                   187           159.0\n",
       "Kings XI Punjab                  176           158.0\n",
       "Sunrisers Hyderabad              108           158.0\n",
       "Royal Challengers Bangalore      180           156.0\n",
       "Kolkata Knight Riders            178           154.0\n",
       "Rajasthan Royals                 146           154.0\n",
       "Rising Pune Supergiant            16           154.0\n",
       "Deccan Chargers                   75           153.0\n",
       "Delhi Daredevils                 161           151.0\n",
       "Rising Pune Supergiants           14           147.0\n",
       "Pune Warriors                     45           141.0\n",
       "Kochi Tuskers Kerala              14           136.0"
      ]
     },
     "execution_count": 347,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "a.sort_values(by='Team avg score',ascending=False)[['Matches','Team avg score']]"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
