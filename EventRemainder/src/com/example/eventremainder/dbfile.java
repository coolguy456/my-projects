package com.example.eventremainder;

import android.content.ContentValues;
import android.content.Context;
import android.database.Cursor;
import android.database.DatabaseUtils;
import android.database.sqlite.SQLiteDatabase;
import android.database.sqlite.SQLiteDatabase.CursorFactory;
import android.database.sqlite.SQLiteOpenHelper;

public class dbfile extends SQLiteOpenHelper{
	
   public final static String elist = " elist ";
   public final static String id = "_id";   
   public final static String name = "name";
   public final static String number = "number";
   public final static String eventcategory = "eventcategory";
   public final static String message = "message";
   public final static String hour = "hour";
   public final static String minute = "minute";
   public final static String month = "month";
   public final static String year = "year";
   public final static String ringtone = "ringtone";
   public final static String date = "date";
   public final static String ainsmod = "ainsmod";
   public static String databasename = "databasename.db";
   public static  int databaseversion = 1;
   public String shared = "shared";
   
    	public String dbcommand="create table" + elist + " ( " + id + " integer primary key autoincrement, "  
	
	+ name + " text, "
	+ number + " text, "
	+ eventcategory + " text, "
	+ message + " text, "
	+ ringtone + " text, "
	+ ainsmod + " integer, "
	+ hour + " integer, "
	+ minute + " integer, "
	+ date + " integer, "
	+ month + " integer, "
	+ year + " integer " + " ) ";
   
   	

	public dbfile(Context context, String name, CursorFactory factory,
			int version) {
		super(context, name, factory, version);
	     	}
  public dbfile(Context context){
	  super(context, databasename , null , 1);
  }

	@Override
	public void onCreate(SQLiteDatabase eb) {
		eb.execSQL(dbcommand);
		
	}
	
	

	@Override
	public void onUpgrade(SQLiteDatabase eg, int oldVersion, int newVersion) {
		eg.execSQL("DROP TABLE IF EXISTS "+elist);
	      onCreate(eg);
			}
	
	public void entry(entry e){
	SQLiteDatabase db = this.getWritableDatabase();db.beginTransaction();
db.execSQL("insert into elist (name,number,eventcategory,message,ringtone,ainsmod,hour,minute,date,month,year) " +
		"  values ('"+e.name+"','"+e.number+"','"+e.eventcategory+"','"+e.message+"','"+e.ringtone+"','"+e.ainsmode+"','"+e.hour+"','"+e.minute+"','"+e.date+"','"+e.month+"','"+e.year+"')");
db.setTransactionSuccessful();
db.endTransaction();db.close();	}


	public int hc(){
		SQLiteDatabase db = this.getReadableDatabase();db.beginTransaction();
	      Integer numRows = (int) DatabaseUtils.queryNumEntries(db, elist);
	      db.setTransactionSuccessful();db.endTransaction();
	      db.close();
	      return numRows;
	   }
	public void delete(int gbd){Integer fr=this.hc();
		SQLiteDatabase db = this.getWritableDatabase();db.beginTransaction();
		
		Integer gd = gbd;Integer sd;
		
		db.execSQL("DELETE FROM elist WHERE _id="+gd.toString());
		
		for(sd=gd+1;sd<fr+1;sd++){Integer sdd=sd-1;
		db.execSQL("UPDATE elist set _id="+"'"+sdd.toString()+"'"+"where _id="+"'"+sd.toString()+"'");}
		db.setTransactionSuccessful();db.endTransaction();db.close();
		
		
	}
	public void upyear(int i){Integer u = i;Integer y = u+1;
		SQLiteDatabase db = this.getWritableDatabase();
		db.beginTransaction();
		Cursor t = db.rawQuery("update elist set year='"+y.toString()+"'"+" where year='"+u.toString()+"'", null);
		db.setTransactionSuccessful();
		db.endTransaction();t.close();db.close();
	}
	
	public void onchangevalues(entry e,int hd){SQLiteDatabase db = this.getWritableDatabase();
		ContentValues ti = new ContentValues();Integer fd=hd;
		ti.put(name,e.name);
		ti.put(message,e.message);
			ti.put(ainsmod, e.ainsmode);
			ti.put(eventcategory,e.eventcategory);
			ti.put(ringtone,e.ringtone);
			ti.put(date,e.date);ti.put(month, e.month);ti.put(year, e.year);
			ti.put(hour, e.hour);ti.put(minute, e.minute);
			ti.put(number, e.number);
			db.beginTransaction();
			db.update(elist, ti, "_id=?",new String[]{ Integer.toString(fd) });
			db.setTransactionSuccessful();db.endTransaction();db.close();}
	
	public  String thename(int id){Integer dd=id;String finalname = null;
		SQLiteDatabase dg = this.getReadableDatabase();
		dg.beginTransaction();
Cursor c = dg.rawQuery("SELECT name from  elist  where _id="+Integer.toString(dd),null);
if(c.moveToNext()){
finalname  = c.getString(0);c.close();dg.setTransactionSuccessful();
		dg.endTransaction();dg.close();
	
		return finalname;}else 
			c.close();
		dg.setTransactionSuccessful();dg.endTransaction();dg.close();
			return null;}
	
	
	public  int theains(int id){Integer dd=id;int finalname = 0;
	SQLiteDatabase dg = this.getReadableDatabase();
	dg.beginTransaction();
Cursor c = dg.rawQuery("SELECT ainsmod from  elist  where _id="+Integer.toString(dd),null);
if(c.moveToNext()){
finalname  = c.getInt(0);c.close();dg.setTransactionSuccessful();
	dg.endTransaction();dg.close();

	return finalname;}else 
		c.close();
	dg.setTransactionSuccessful();dg.endTransaction();dg.close();
		return 5;}
	public int theyear(int id){Integer dd=id;int finalname = 0;
	SQLiteDatabase dg = this.getReadableDatabase();
	dg.beginTransaction();
Cursor c = dg.rawQuery("SELECT year from  elist  where _id="+Integer.toString(dd),null);
if(c.moveToNext()){
finalname  = c.getInt(0);c.close();dg.setTransactionSuccessful();
	dg.endTransaction();dg.close();

	return finalname;}else 
		c.close();
	dg.setTransactionSuccessful();dg.endTransaction();dg.close();
		return 5;}
	
	public int thedate(int id){Integer dd=id;int finalname = 0;
	SQLiteDatabase dg = this.getReadableDatabase();
	dg.beginTransaction();
Cursor c = dg.rawQuery("SELECT date from  elist  where _id="+Integer.toString(dd),null);
if(c.moveToNext()){
finalname  = c.getInt(0);c.close();dg.setTransactionSuccessful();
	dg.endTransaction();dg.close();
			return finalname;}else 
		c.close();
	dg.setTransactionSuccessful();dg.endTransaction();dg.close();
		return 5;}
	
	
	public int themonth(int id){Integer dd=id;int finalname = 0;
	SQLiteDatabase dg = this.getReadableDatabase();
	dg.beginTransaction();
Cursor c = dg.rawQuery("SELECT month from  elist  where _id="+Integer.toString(dd),null);
if(c.moveToNext()){
finalname  = c.getInt(0);c.close();dg.setTransactionSuccessful();
	dg.endTransaction();dg.close();

	return finalname;}else 
		c.close();
	dg.setTransactionSuccessful();dg.endTransaction();dg.close();
		return 5;}
	
	
	public int thehour(int id){Integer dd=id;int finalname = 0;
	SQLiteDatabase dg = this.getReadableDatabase();
	dg.beginTransaction();
Cursor c = dg.rawQuery("SELECT hour from  elist  where _id="+Integer.toString(dd),null);
if(c.moveToNext()){
finalname  = c.getInt(0);c.close();dg.setTransactionSuccessful();
	dg.endTransaction();dg.close();

	return finalname;}else 
		c.close();
	dg.setTransactionSuccessful();dg.endTransaction();dg.close();
		return 5;}
	
	public int theminute(int id){Integer dd=id;int finalname = 0;
	SQLiteDatabase dg = this.getReadableDatabase();
	dg.beginTransaction();
Cursor c = dg.rawQuery("SELECT minute from  elist  where _id="+Integer.toString(dd),null);
if(c.moveToNext()){
finalname  = c.getInt(0);c.close();dg.setTransactionSuccessful();
	dg.endTransaction();dg.close();

	return finalname;}else 
		c.close();
	dg.setTransactionSuccessful();dg.endTransaction();dg.close();
		return 5;}
	
	
	
	
	
	
	
	
	
	
	
	public  String ther(int id){Integer dd=id;String finalname = null;
	SQLiteDatabase dg = this.getReadableDatabase();
	dg.beginTransaction();
Cursor c = dg.rawQuery("SELECT ringtone from  elist  where _id="+Integer.toString(dd),null);
if(c.moveToNext()){
finalname  = c.getString(0);c.close();dg.setTransactionSuccessful();
	dg.endTransaction();dg.close();

	return finalname;}else 
		c.close();
	dg.setTransactionSuccessful();dg.endTransaction();dg.close();
		return null;}
	
	
	
	
	
	
	
	
	
	
	
	
	
	public  String themessage(int id){Integer dd=id;String finalname = null;
	SQLiteDatabase dg = this.getReadableDatabase();
	dg.beginTransaction();
Cursor c = dg.rawQuery("SELECT message from  elist  where _id="+Integer.toString(dd),null);
if(c.moveToNext()){
finalname  = c.getString(0);c.close();dg.setTransactionSuccessful();
	dg.endTransaction();dg.close();

	return finalname;}else 
		c.close();
	dg.setTransactionSuccessful();dg.endTransaction();dg.close();
		return null;}
	
	public  String thenumber(int id){Integer dd=id;String finalname = null;
	SQLiteDatabase dg = this.getReadableDatabase();
	dg.beginTransaction();
Cursor c = dg.rawQuery("SELECT number from  elist  where _id="+Integer.toString(dd),null);
if(c.moveToNext()){
finalname  = c.getString(0);c.close();dg.setTransactionSuccessful();
	dg.endTransaction();dg.close();

	return finalname;}else 
		c.close();
	dg.setTransactionSuccessful();dg.endTransaction();dg.close();
		return null;}
	
	
	
	
	
	
	
	
	
	
	public  String theevent(int id){Integer dd=id;String finalname = null;
	SQLiteDatabase dg = this.getReadableDatabase();
	dg.beginTransaction();
Cursor c = dg.rawQuery("SELECT eventcategory from  elist  where _id="+Integer.toString(dd),null);
if(c.moveToNext()){
finalname  = c.getString(0);c.close();dg.setTransactionSuccessful();
	dg.endTransaction();dg.close();

	return finalname;}else 
		c.close();
	dg.setTransactionSuccessful();dg.endTransaction();dg.close();
		return null;}
	
	
	
	public int lastid(){int theid = 0;
	 String[] is = {dbfile.id};
     SQLiteDatabase dg = this.getReadableDatabase();
     dg.beginTransaction();
     Cursor c1 = dg.query(dbfile.elist,is, null, null, null, null,null);	
     if(c1.moveToFirst()){					 		 	 			 				 
	c1.moveToLast();
	theid = c1.getInt(c1.getColumnIndex(dbfile.id));	}c1.close();
	dg.setTransactionSuccessful();dg.endTransaction();dg.close();
	
	return theid;}
	
	
public void close(){SQLiteDatabase db = this.getReadableDatabase();
           if(db != null & db.isOpen()){db.close();}
           }
	}
