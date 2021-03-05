open the template in the editor.
 */
package tpcrypto;
import java.security.*;
import javax.crypto.*;
import java.security.NoSuchAlgorithmException;
import java.util.Random;

/**
 *
 * @author hp
 */
public class TPcrypto {

    /**
     * @param args the command line arguments
     */
    //LA FONCTION QUI CONVERTIE UN HEXADECIMAL EN DECIMAL
   
    public static void main(String[] args) throws NoSuchAlgorithmException {
        // TODO code application logic here

         //VERIFFICATION QUE DECIMAL MARCHE
       //System.out.println(decimal("A"));
       
       Random rand= new Random();
       
       String id="bettiouifarid";
       String x;
     
      
       double i;
       double count=0;
       String Y="03b1663dda6549a0939ffdd712a852e0d4234e6b";
       
      for (i=0;;i++)
      {
          count=i; 
      
         int comp=sha1(id+rand.nextInt()).compareTo(Y);
         if (comp<=0)
         {
          break;
         }
      }
        System.out.println("le resultat de SH1 (id||x):");
        System.out.println(sha1(id+val));
        System.out.println(" X est egal �:");
        System.out.println(rand.nextInt());
        System.out.println("le nombre d'iteration pour trouver le X est egal �");
        System.out.println(count);
    }


    static String sha1(String input) throws NoSuchAlgorithmException {
        MessageDigest mDigest = MessageDigest.getInstance("SHA1");
        byte[] result = mDigest.digest(input.getBytes());
        StringBuffer sb = new StringBuffer();
        for (int i = 0; i < result.length; i++) {
            sb.append(Integer.toString((result[i] & 0xff) + 0x100, 16).substring(1));
        }
         
        return sb.toString();
    }

    private static int sh1(String chaine) {
        throw new UnsupportedOperationException("Not supported yet."); //To change body of generated methods, choose Tools | Templates.
    }
}