var sale = new Sale();
var beer = new Beer();

Some(sale);
Some(beer);

void Some(ISave save) // Puedo usar cualquier funcion que implemente ISave
{
    save.Save();
}
interface ISale
{
    decimal Total { get; set; }
}
interface ISave
{
    public void Save();
}


public class Sale : ISale, ISave
{
    public decimal Total { get; set; }

    public void Save()
    {
        Console.WriteLine("Se guardo en BD");
    }
}

public class Beer : ISave
{
    public void Save()
    {
        Console.WriteLine("Se guardo el servicio");
    }
}