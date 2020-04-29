
package kargo;

import java.nio.charset.Charset;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;
import java.util.ArrayList;
import java.util.LinkedHashMap;
import java.util.Random;
import java.util.logging.Level;
import java.util.logging.Logger;
import javax.swing.SpringLayout;

public class Database {
    private String userName = "root";
    private String parola = "";
    private String databaseName = "cargo";
    private String host = "localhost";
    private int port = 3306;
    private Connection con = null;
    private Statement statement = null;
    private PreparedStatement preparedStatement = null;
    
    public Database(){
        String url = "jdbc:mysql://" + host + ":" 
                + port + "/" + databaseName 
                + "?useUnicode=true&characterEncoding=utf8";    
        
        try{
            Class.forName("com.mysql.jdbc.Driver");
        } catch (ClassNotFoundException ex) {
            System.out.println("Driver Not Found");
            System.exit(0);
        }
        
        try {
            con = DriverManager.getConnection(url, userName, parola);
        } catch (SQLException ex) {
            System.out.println("Connection Failed");
            System.exit(0);
        }
    }
    
    public ArrayList<String[]> getCargo(){
	String sorgu = "Select * from packages";
	ArrayList<String[]> packages = new ArrayList<>();
        String[] cargo = new String[9];
	try{
		statement = con.createStatement();
	    ResultSet rs = statement.executeQuery(sorgu);
		while(rs.next()){
			 cargo[0] = rs.getString("TrackNo");
                         cargo[1] = rs.getString("SenderName");
                         cargo[2] = rs.getString("SenderNumber");
                         cargo[3] = rs.getString("SenderAddress");
                         cargo[4] = rs.getString("RecipientName");
                         cargo[5] = rs.getString("RecipientNumber");
                         cargo[6] = rs.getString("AddresstobeDelivered");
                         cargo[7] = rs.getString("FragilePackage");
                         cargo[8] = rs.getString("State");
                         packages.add(cargo);
		}
                statement.executeQuery(sorgu);

	
	} catch (SQLException ex) {
            Logger.getLogger(Database.class.getName()).log(Level.SEVERE, null, ex);
        }
        return packages;
    }
    
    public void addCargo(String[] info,String trackNo){
        
        String sorgu = "INSERT INTO packages (TrackNo,SenderName,SenderNumber"
                + ",SenderAddress,RecipientName,RecipientNumber,AddresstobeDelivered"
                + ",Weight,Volume,FragilePackage,State)"
                +" VALUES(?,?,?,?,?,?,?,?,?,?,?)";
	try{
		preparedStatement = con.prepareStatement(sorgu);
                for(int i=2;i<=10;i++){
                    preparedStatement.setString(i, info[i-2]);
                }
                preparedStatement.setString(1,trackNo);
                preparedStatement.setString(11,info[2]);
                
		preparedStatement.executeUpdate();
		
	} catch (SQLException ex) {
            Logger.getLogger(Database.class.getName()).log(Level.SEVERE, null, ex);
        }

    }
    
    public void packageArrived(String trackNo){
	
        String sorgu = "DELETE FROM packages WHERE TrackNo = '" + trackNo + "'";
	
	try{	
            preparedStatement = con.prepareStatement(sorgu);
            //preparedStatement.setString(1, trackNo);	
            preparedStatement.executeUpdate(sorgu);
		
	} catch (SQLException ex) {
            Logger.getLogger(Database.class.getName()).log(Level.SEVERE, null, ex);
        }
	
	

    }
    
    public void updateCargo(String trackNo,String SenderName,String SenderNumber
    ,String SenderAddress,String RecipientName, String RecipientNumber
    ,String AddresstobeDelivered,String FragilePackage,String State){
        
        String sorgu = "UPDATE packages SET SenderName = ?,SenderNumber = ?"
                + ",SenderAddress = ?, RecipientName = ?, RecipientNumber = ?"
                + ",AddresstobeDelivered = ?,FragilePackage = ?,State = ? WHERE TrackNo = ?";
        
        try {
            preparedStatement = con.prepareStatement(sorgu);
            preparedStatement.setString(1, SenderName);
            preparedStatement.setString(2, SenderNumber);
            preparedStatement.setString(3, SenderAddress);
            preparedStatement.setString(4, RecipientName);
            preparedStatement.setString(5, RecipientNumber);
            preparedStatement.setString(6, AddresstobeDelivered);
            preparedStatement.setString(7, FragilePackage);
            preparedStatement.setString(8, trackNo);
            preparedStatement.setString(9, State);
            preparedStatement.executeUpdate();
            
            
        } catch (SQLException ex) {
            Logger.getLogger(Database.class.getName()).log(Level.SEVERE, null, ex);
        }
        
    }
    
    public LinkedHashMap<String,String> getStaff(){
        String sorgu = "Select * from staff";
	LinkedHashMap<String,String> info = new LinkedHashMap<>();
	try{
		statement = con.createStatement();
	    ResultSet rs = statement.executeQuery(sorgu);
		while(rs.next()){
                    info.put(rs.getString("UserName"),rs.getString("Password"));
		}
                statement.executeQuery(sorgu);
	
	} catch (SQLException ex) {
            Logger.getLogger(Database.class.getName()).log(Level.SEVERE, null, ex);
        }
        return info;
        
    }
    
    public String track(String trackNo){
        String command;
        command = "Select * from packages where TrackNo = '" + trackNo + "'";
        try{
            statement = con.createStatement();
            ResultSet rs = statement.executeQuery(command);
            if(rs.next())
                return rs.getString("State");
            else
                return null;
            
        } catch (SQLException ex) {
            System.err.println("Track Number Not Found Error");
            return null;
        }
    }
    
    public int getDistance(String city1, String city2){
        String command;
        command = "Select " + city1 + " from distances where City = '" + city2 + "'";
        
        try{
            statement = con.createStatement();
            ResultSet rs = statement.executeQuery(command);
            if(rs.next()){
                return rs.getInt(city1);
            }
        } catch (SQLException ex) {
            Logger.getLogger(Database.class.getName()).log(Level.SEVERE, null, ex);

        }
        return 0;
        
    }
    
    public String getOffice(String city){
        String command = "SELECT Address FROM offices WHERE City = '" + city + "'";
        String adr = "";
        try{
            statement = con.createStatement();
            ResultSet rs = statement.executeQuery(command);
            if(rs.next()){
            adr =  rs.getString("Address");
            }
        } catch (SQLException ex){
            Logger.getLogger(Database.class.getName()).log(Level.SEVERE, null, ex);
        }
        return adr;
    }
    
    
    
    
}
