![image](https://user-images.githubusercontent.com/49811782/135673141-466db176-7646-4f2c-b886-87c0123c6c95.png)

# About the Project 📊
Pokemon is one of the famous cartoon series which is been loved by all age group people. Different types of Pokemons and their powers along with journey with their trainers is quite interesting and amazing. The Pokemon Dashboard project is a fun data analytics project which is made with curiosity to make something different. As I am a Pokemon fan, developing this project was a fun task for me.

# Key Features of the Project 🔥

👉 There are some Pokemon dashboard projects available on the internet, but the project developed here is unique and cannot be found anywhere else.

👉 The evolution page of the project is a bit different from other dashboards.

👉 The dataset used in the project is not available anywhere on the internet. The dataset and images were created by web scraping various websites.

👉 If you have seen the Pokemon cartoon, each trainer has a Pokedex with them. Here, we have tried to make a similar kind of Pokedex, but it is a virtual one. 😂😂

# Tools Used 🛠️

<table align="center">
  <tr>
    <td align="center" width="96">
     <a href="#" target="_blank">
      <img loading="lazy" src="https://www.vectorlogo.zone/logos/microsoft_powerbi/microsoft_powerbi-icon.svg" alt="power-bi" width="40" height="40"/> 
    </a>
    <br/>PowerBI
   </td>
   <td align="center" width="96">
    <a href="#" target="_blank"> 
     <img loading="lazy" src="https://webobjects2.cdw.com/is/image/CDW/5300125?$product-main$" alt="excel" width="40" height="40"/>
    </a>
    <br/> Excel
   </td>
   <td align="center" width="96">
      <a href="#">
        <img loading="lazy" src="https://img.icons8.com/?size=512&id=ITIhejPZQD5g&format=png" alt="web-scrapper" width="100" height="60"/>
      </a>
      <br> WebScrapper
    </td>
    <td align="center" width="96">
      <a href="#">
        <img loading="lazy" src="https://i0.wp.com/junilearning.com/wp-content/uploads/2020/06/python-programming-language.webp?fit=1920%2C1920&ssl=1" alt="Python" width="100" height="60"/>
      </a>
      <br> Python
    </td>
  </tr>
</table>

# About the Dataset 📝

👉 **Pokemon Details**: The first dataset contains various details such as types, species, growth, abilities, attack score, HP score, defense score, resistance against different types of Pokemon, and most importantly, their images.

👉 **Pokemon Evolution Dataset**: The dataset includes images of Pokemon evolution from level 1 to level 3.

👉 **Pokemon Description Dataset**: This dataset contains descriptions of various Pokemons.

👉 **Pokemon Types Images Dataset**: The dataset includes various images representing Pokemon types such as water, fire, grass, electric, etc.


# 🔊 Text-to-Speech Feature
This project includes a **text-to-speech (TTS) feature** that reads out Pokemon descriptions using Python's `pyttsx3` library. This enhances the interactive experience, making it feel more like a real Pokedex.

### Python Script Used:
```python
import matplotlib.pyplot as plt
import pyttsx3

# Initialize text-to-speech engine
engine = pyttsx3.init()
engine.setProperty('rate', 155)  # Adjust speed
engine.setProperty('volume', 1.0)  # Max volume

# Check if "Description" exists in dataset
if "Description" in dataset.columns and not dataset["Description"].isna().all():
    text = dataset["Description"].iloc[0]
    engine.say(text)
    engine.runAndWait()  # Speak the description

# Keep a dummy plot displayed so Power BI doesn't throw an error
plt.figure(figsize=(2, 1))
plt.text(0.5, 0.5, "", fontsize=12, ha="center")
plt.axis("off")
plt.show()
```

# 📷 Dashboard Outputs
Below are some visuals from the Power BI dashboard, showcasing Pokemon statistics, evolution trends, and insights from the dataset.

![Dashboard Screenshot](output/final%20output_page-0001.jpg)


![Dashboard Screenshot](output/final%20output_page-0002.jpg)


![Dashboard Screenshot](output/final%20output_page-0003.jpg)

---

# 🌟 Future Enhancements
- **Adding Interactive Filters**: Allow users to dynamically explore Pokemon stats based on type, strength, and abilities.
- **Integration with External APIs**: Fetch live Pokemon data to keep the dashboard updated.
- **Performance Optimization**: Improve data processing and visualization speed.

🚀 Stay tuned for more updates!
