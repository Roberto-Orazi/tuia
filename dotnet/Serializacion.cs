using System.Text.Json;

var hector = new People()
{
    Name = "Hector",
    Age = 36
};

string json = JsonSerializer.Serialize(hector);
Console.WriteLine(json);

string myJson = @"{
    ""Name"":""Jorge"",
     ""Age"":36
}";

People? jorge = JsonSerializer.Deserialize<People>(myJson);
Console.WriteLine(jorge?.Name);
Console.WriteLine(jorge.Age);

public class People
{
    public string Name { get; set; }
    public int Age { get; set; }
}