// El var es para ahorrarse escribir Sale, podemos ver que podemos escribirlo de cualquiera de esas 3 maneras

// Sale sale = new Sale();

// Sale sale = new();
var sale = new Sale(15, 1.16m);

var message = sale.GetInfo();
Console.WriteLine(message);

class SaleWithTax : Sale
{
    public decimal Tax { get; set; }
    public SaleWithTax(decimal total, decimal tax) : base(total)
    {
        Tax = tax;
    }
    public override string GetInfo()
    {
        return "El total es" + Total + "Impuesto es:" + Tax;
    }
    public string GetInfo(string message)
    {
        return message;
    }
    public string GetInfo(int a)
    {
        return a.ToString();
    }
}

class Sale
{
    public decimal Total { get; set; }

    public Sale(decimal total)
    {
        Total = total;
    }

    public virtual string GetInfo() // Se usa virtual en el padre y override en el hijo
    {
        return "El total es" + Total;
    }
}

