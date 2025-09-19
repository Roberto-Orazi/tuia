var numbers = new MyList<int>(5);
var names = new MyList<string>(5);
var beers = new MyList<Beer>(3);

numbers.Add(1);
numbers.Add(2);
numbers.Add(3);
numbers.Add(4);
numbers.Add(5);
numbers.Add(6);
names.Add("Roberto");
names.Add("Ana");
names.Add("Juan");
names.Add("Jorge");
names.Add("Carla");
names.Add("Carlos");

beers.Add(new Beer()
{
    Name = "Erdinger",
    Price = 5
});
beers.Add(new Beer()
{
    Name = "Corona",
    Price = 1
});
beers.Add(new Beer()
{
    Name = "Heineken",
    Price = 10
});
beers.Add(new Beer()
{
    Name = "Delirium",
    Price = 5
});

Console.WriteLine(numbers.GetContent());
Console.WriteLine(names.GetContent());

public class MyList<T>
{
    private MyList<T> _list;
    private int _limit;

    public MyList(int limit)
    {
        _limit = limit;
        _list = new List<T>();
    }
    public void Add(T element)
    {
        if (_list.Count < limit)
        {
            _list.Add(element);
        }
    }
    public string GetContent()
    {
        string content = "";
        foreach (var element in _list)
        {
            content += element + ", ";
        }
        return content;
    }
}

public class Beer()
{
    public string Name { get; set; }
    public decimal Price { get; set; }

    public override string ToString()
    {
        return "Nombre: " + Name + "Price: " + Price ;
    }
}