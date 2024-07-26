class Config:
    API_PREFIX = '/api/v1'
    
    API_LLM = 'http://192.168.1.1:1234/v1'
    API_KEY = 'lm-studio'
    
    ML_MODEL = 'app/u_proof_stacking_model.pkl'

    MODELS = ["TheBloke/Mistral-7B-Instruct-v0.2-GGUF/mistral-7b-instruct-v0.2.Q8_0.gguf", 
              "lmstudio-community/Meta-Llama-3.1-8B-Instruct-GGUF/Meta-Llama-3.1-8B-Instruct-Q8_0.gguf"]

    PROMPT = """ In the role of a cybersecurity expert, using the website URL provided,
                evaluate whether the site could be a phishing site.
                You have to decide wLhether to visit the website for the first time with the
                url: "[url_here]".
                Determine whether the site might be a phishing or legitimate site.
                Provide an explanation of your decision, highlighting the signals you
                considered in reaching that conclusion and providing a representation based
                on a numerical bullet list.
                Note, if you can't access the site justify your answer and in case the site
                doesn't exist tell me and based on the link to see if it is a phishing site.
                Response:
                I only want you to return only and only a JSON of this type and make sure to
                reply only with the json:
                {
                "url": [inserted url],
                "prediction": [Prediction value 0 is for Legitimate, 1 for Phishing],
                "proba": [Prediction probability]
                "motivation": "[Enter the model's decision rationale here]"
                }
            """