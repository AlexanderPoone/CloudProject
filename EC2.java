import com.amazonaws.AmazonServiceException;
import com.amazonaws.services.s3.*;
import com.amazonaws.services.s3.model.*;

import java.io.*;
import java.nio.file.Paths;
import java.util.*;

public class S3 {

  static {
    System.setProperty("https.proxyHost", "");
    System.setProperty("https.proxyPort", "8000");
    System.setProperty("http.proxyHost", "");
    System.setProperty("http.proxyPort", "8000");
  }

  public static void usage() {
    System.out.println("Usage: ");
    System.out.println("    java -cp .:./lib/* S3APIDemo upload [local_file_name] [remote_file_name]");
    System.out.println("    java -cp .:./lib/* S3APIDemo download [remote_file_name] [local_file_name]");
    System.out.println("    java -cp .:./lib/* S3APIDemo delete [file_name]");
  }
  
  public static void main(String[] args) {
    if (args.length < 1) {
      usage();
      System.exit(1);
    }
    
    String operation = args[0];

    final AmazonS3 s3 = AmazonS3ClientBuilder.defaultClient();

    List<Bucket> buckets = s3.listBuckets();
    System.out.println("Your Amazon S3 buckets are:");
    for (Bucket b : buckets) {
        System.out.println("* " + b.getName());
	}

    Bucket b = null;
    String bucket_name = "csci4180bucket";
    if (s3.doesBucketExist(bucket_name)) {
      System.out.format("Bucket %s already exists.\n", bucket_name);
      b = getBucket(bucket_name);
    } else {
      try {
        b = s3.createBucket(bucket_name);
      } catch (AmazonS3Exception e) {
        System.err.println(e.getErrorMessage());
      }
    }

    if (operation.equals("upload")) {
      if (args.length < 3) {
        usage();
	System.exit(1);
      }
      
      String localFileName = args[1];
      String remoteFileName = args[2];

      try {
        s3.putObject(bucket_name, remoteFileName, new File(localFileName));
      } catch (AmazonServiceException e) {
        System.err.println(e.getErrorMessage());
        System.exit(1);
      }
    } else if (operation.equals("download")) {
      if (args.length < 3) {
        usage();
	System.exit(1);
      }
      
      String remoteFileName = args[1];
      String localFileName = args[2];

      try {
        S3Object o = s3.getObject(bucket_name, remoteFileName);
	S3ObjectInputStream s3is = o.getObjectContent();
	FileOutputStream fos = new FileOutputStream(new File(localFileName));
	byte[] read_buf = new byte[1024];
	int read_len = 0;
	while ((read_len = s3is.read(read_buf)) > 0) {
	  fos.write(read_buf, 0, read_len);
	}
	s3is.close();
	fos.close();
      } catch (AmazonServiceException e) {
        System.err.println(e.getErrorMessage());
	System.exit(1);
      } catch (FileNotFoundException e) {
        System.err.println(e.getMessage());
        System.exit(1);
      } catch (IOException e) {
        System.err.println(e.getMessage());
        System.exit(1);
      }
    } else if (operation.equals("delete")) {
      if (args.length < 2) {
        usage();
	System.exit(1);
      }
      
      String fileName = args[1];

      try {
        s3.deleteObject(bucket_name, fileName);
      } catch (AmazonServiceException e) {
        System.err.println(e.getErrorMessage());
	System.exit(1);
      }
    }
  }

  public static Bucket getBucket(String bucket_name) {
    final AmazonS3 s3 = AmazonS3ClientBuilder.defaultClient();
    Bucket named_bucket = null;
    List<Bucket> buckets = s3.listBuckets();
    for (Bucket b : buckets) {
      if (b.getName().equals(bucket_name)) {
        named_bucket = b;
      }
    }
    return named_bucket;
  }
}
