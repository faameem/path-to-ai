import org.apache.storm.Config;
import org.apache.storm.StormSubmitter;
import org.apache.storm.generated.StormTopology;
import org.apache.storm.topology.TopologyBuilder;


public class Topology3Bolts {
    public static void main(String[] args) throws InterruptedException {

        //Build Topology
        TopologyBuilder builder = new TopologyBuilder();
        builder.setSpout("Yahoo-Finance-Spout", new yfSpout());
        builder.setBolt("Yahoo-Finance-Bolt", new yfBolt(),3)
                .shuffleGrouping("Yahoo-Finance-Spout");

        StormTopology topology = builder.createTopology();
        //Configuration
        Config conf = new Config();
        conf.setDebug(true);
        conf.put("fileToWrite", "/Users/swethakolalapudi/Desktop/yfOutput/output.txt");

        //Submit Topology to cluster
        try{
            StormSubmitter.submitTopology("Parallelized-Topology", conf, topology);
        }catch (Exception e){
            e.printStackTrace();
        }
    }


}
