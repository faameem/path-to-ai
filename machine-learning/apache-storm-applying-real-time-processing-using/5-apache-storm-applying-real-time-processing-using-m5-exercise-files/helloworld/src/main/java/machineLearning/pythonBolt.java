package machineLearning;

import org.apache.storm.task.ShellBolt;
import org.apache.storm.topology.IRichBolt;
import org.apache.storm.topology.OutputFieldsDeclarer;
import org.apache.storm.tuple.Fields;

import java.util.Map;


public class pythonBolt extends ShellBolt implements IRichBolt {

    public pythonBolt() {
        super("python",
                "/Users/swethakolalapudi/pythonScripts/bolt.py");
    }

    public void declareOutputFields(OutputFieldsDeclarer declarer) {
        declarer.declare(new Fields("sentence","length"));
    }


    public Map<String, Object> getComponentConfiguration() {
        return null;
    }

    }