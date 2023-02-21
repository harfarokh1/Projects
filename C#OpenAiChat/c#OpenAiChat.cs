using System;
using System.Net.Http;
using System.Text;
using System.Threading.Tasks;
using Newtonsoft.Json;

class Program
{
    static async Task Main(string[] args)
    {
        // Set your API key and the model name
        string API_KEY = "APIKEY";
        string model = "text-davinci-003";

        // Set the prompt and other parameters for generating text e.g max tokens etc
        string prompt = "";
        Console.Write("Please enter a question: ");
        prompt = Console.ReadLine();
        int maxTokens = 1000;
        double temperature = 0.9;

        // Set up the HTTP client and request
        HttpClient httpClient = new HttpClient();
        string url = "https://api.openai.com/v1/completions";
        httpClient.DefaultRequestHeaders.Add("Authorization", "Bearer " + API_KEY);
        string requestBody = JsonConvert.SerializeObject(new
        {
            model = model,
            prompt = prompt,
            max_tokens = maxTokens,
            temperature = temperature
        });
        var content = new StringContent(requestBody, Encoding.UTF8, "application/json");
        var response = await httpClient.PostAsync(url, content);

        // Read and output the response
        string responseString = await response.Content.ReadAsStringAsync();
        dynamic jsonResponse = JsonConvert.DeserializeObject(responseString);
        string generatedText = jsonResponse.choices[0].text;
        Console.WriteLine(generatedText);
    }
}