import openai, json
from app.config import Config

def send_prompt_llm(prompt, models):
    # Point to the local server
    client = openai.OpenAI(base_url=Config.API_LLM, api_key=Config.API_KEY)

    responses = []
    for model in models:
        try:
            response = client.chat.completions.create(
                model=model,
                response_format={ "type": "json_object" },
                messages=[
                    {"role": "system", "content": "You are a helpful assistant designed to output only JSON."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.7
            )
            responses.append({
                "model": model,
                "response": response.choices[0].message.content
            })
        except Exception as e:
            responses.append({
                "model": model,
                "response": f"Error: {str(e)}"
            })

    return {
        "prompt": prompt,
        "responses": responses
    } 

def get_llm_response(prompt, models):
    llm_response = send_prompt_llm(prompt, models)["responses"]
    return [json.loads(r['response']) for r in llm_response]