import java.io.RandomAccessFile;

public class Main {
    public static void main(String[] argv) throws Exception {
      RandomAccessFile raf = new RandomAccessFile();
  
      int len;
      byte data[] = new byte[16];
  
      // Read bytes until EOF is encountered.
      do {
        len = raf.read(data);
        for (int j = 0; j < len; j++)
          System.out.printf("%02X ", data[j]);
      } while (len != -1);
    }
  }