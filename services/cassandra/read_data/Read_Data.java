import com.datastax.driver.core.Cluster;
import com.datastax.driver.core.ResultSet;
import com.datastax.driver.core.Session;

public class Read_Data {

   public static void main(String args[])throws Exception{
    
      //queries
      String import = "COPY input ( index_id, id, news_url, title, tweet_ids, Y, category) FROM '/home/fake-news-detection/src/data/combined_shufled_data_import.csv'";
      String query = "SELECT * FROM input";

      //Creating Cluster object 
      Cluster cluster = Cluster.builder().addContactPoint("127.0.0.1").build();
    
      //Creating Session object - use keyspace
      Session session = cluster.connect("fakenews");
    
      //Getting the ResultSet
      ResultSet result = session.execute(import);
      ResultSet result = session.execute(query);
    
      System.out.println(result.all());
   }
}
