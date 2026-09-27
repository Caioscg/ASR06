module Demo
{
    // Excecao remota lancada pelo servidor e recebida pelo cliente
    exception DivisionByZero
    {
        string reason;
    }

    interface Printer
    {
        // Metodo original do exemplo
        string printString(string s);

        // Metodos novos (ASR 06)
        string toUpperCase(string s);
        string reverseString(string s);
        int countWords(string s);
        int add(int a, int b);
        double divide(double a, double b) throws DivisionByZero;
    }
}
