# Live Server
- fast api
- code: backend/app
- deployed: railway.com
- URL:  quran-rag-backend-production.up.railway.app/docs

# Live frontend
- streamlit
- code: backend/fronted
- deployed: https://streamlit.io/cloud
- URL:  https://quran-rag-frontend-7hdwh8xq7acjkhvfsk4gqf.streamlit.app/

# Live Vector DB
- Qdrant: https://qdrant.tech/
- URL:  https://d11670de-47bc-4a14-8b3a-c495cb7dc19d.eu-central-1-0.aws.cloud.qdrant.io:6333

# Test Input Samples
- *.json

# Compile And Run

1. uv venv
2. .venv\Scripts\activate
3. uv pip install -r requirements.txt

Create .env file and set these keys in that file
-  GOOGLE_API_KEY
-  HF_TOKEN
-  OPENAI_API_key
-  QDRANT_URL
-  QDRANT_API_KEY

#### Open Terminal and run following command
4. uvicorn backend.app.main:app --reload

##### - Note : Only first time It take time to download pytorch_models or safe.tensor models . Please be patient. then click on.

5. Open your browser and navigate to http://127.0.0.1:8000/docs

#### Open Another Terminal And Run the following command
6. streamlit run backend.frontend.frontend.py
7. Open a web browser and navigate to http://127.0.0.1:8501/


#### Result should be stored in Json files of Open and Closed Source When Hadiths are submitted through routes or frontend

-------------------------------------------------------------------
### Samples Inputs if using streamlit Frontends :

Sample Input 1 :

حدثنا عبد الله بن الزبير الحميدي، قال: حدثنا سفيان بن عيينة، عن يحيى بن سعيد الأنصاري، قال: أخبرني محمد بن إبراهيم التيمي، عن علقمة بن وقاص الليثي، عن عمر بن الخطاب رضي الله عنه قال: سمعت رسول الله ﷺ يقول:

«إنما الأعمال بالنيات، وإنما لكل امرئ ما نوى، فمن كانت هجرته إلى الله ورسوله فهجرته إلى الله ورسوله، ومن كانت هجرته لدنيا يصيبها أو امرأة ينكحها، فهجرته إلى ما هاجر إليه.»


Click on
- Extract Narrators Chain  - >  CAMel-Lab/bert based arabic camelbert mse ner

##### Note : Only First time it took some time to download the model from hugging face

Check result in this file
- open_source_models_results.json


Click on
- Extract Narrators chain -> Closed Source

Check Result in this file
- closed_source_models_results.json

-----------------------------------------------------

Sampple input 2 :

Muhammad ibn Bashar narrated to us, who said: Ghundar narrated to us, from Shuʿbah, from Abu Ishaq, from al-Aswad, from Abdullah ibn Masʿud رضي الله عنه, who said: The Messenger of Allah ﷺ said:

"Whoever believes in Allah and the Last Day should speak good or remain silent..."


Click on :
- Extract narator Chain -> Close Source

Check result in this file
- closed_source_models_results.json


Click on :

- Extract narator Chain -> Open Source ( dslim/bert-base-NER )
##### Note : It took some time to download the model from hugging face

Check result in this file
- closed_source_models_results.json

------------------------------------------------------------------------------


### If Using Backend Fastapi Swagger UI then sample inputs

sample 1 :



{
  "hadith_text": "حدثنا إسماعيل بن أبي أويس، قال: حدثني مالك، عن الزهري، عن عبيد الله بن عبد الله، عن ابن عباس رضي الله عنهما، قال: قال رسول الله ﷺ: «لو يعطى الناس بدعواهم، لادعى رجال أموال قوم ودماءهم، ولكن البينة على المدعي، واليمين على من أنكر.»",
  "language": "arabic"
}


sample 2 :

{
  "hadith_text": "حدثنا أحمد بن يونس، قال: حدثنا زهير، قال: حدثنا منصور، عن أبي وائل، عن عبد الله، قال: قال النبي ﷺ: «لا حسد إلا في اثنتين: رجل آتاه الله مالا فسلطه على هلكته في الحق، ورجل آتاه الله الحكمة فهو يقضي بها ويعلمها.»",
  "language": "arabic"
}


sample 3 :

{
  "hadith_text": "It was narrated from Yahya bin Bukayr, from Al-Layth, from 'Uqayl, from Ibn Shuhbah, from 'Urwah, from Aisha, that the Messenger of Allah ﷺ said: 'Whoever innovates something in this matter of ours (i.e., Islam), that is not part of it, will have it rejected.'",
  "language": "english"
}


sample 4 :

{
  "hadith_text": "It was narrated from Yahya bin Bukayr, from Al-Layth, from 'Uqayl, from Ibn Shuhbah, from 'Urwah, from Aisha, that the Messenger of Allah ﷺ said: 'Whoever innovates something in this matter of ours (i.e., Islam), that is not part of it, will have it rejected.'",
  "language": "english"
}
