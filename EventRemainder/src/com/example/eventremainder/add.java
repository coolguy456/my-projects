package com.example.eventremainder;

import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.util.Calendar;
import android.app.ActionBar;
import android.app.Activity;
import android.app.AlarmManager;
import android.app.PendingIntent;
import android.content.Context;
import android.content.Intent;
import android.database.Cursor;
import android.database.sqlite.SQLiteDatabase;
import android.media.RingtoneManager;
import android.net.Uri;
import android.os.Bundle;
import android.provider.ContactsContract;
import android.view.Menu;
import android.view.MenuItem;
import android.view.View;
import android.widget.Button;
import android.widget.CheckBox;
import android.widget.DatePicker;
import android.widget.EditText;
import android.widget.TextView;
import android.widget.TimePicker;
import android.widget.Toast;

public class add extends Activity{Context co =this;
	Intent browser;entry e;	
	String name;
	String number="";
	String event;
	String message="";
	String ringtone=null;CheckBox cbox;
	int ainsmode=20;
	int timehour;
	int timeminute;
	static int date;
	dbfile db = new dbfile(this);
	static int month;
	int year;int m;Integer idr;
	EditText namee;EditText numbere;EditText evente;EditText messagee;TextView ringtonee;
	TimePicker timee;
	Button rp;Button cp;DatePicker pic;Calendar now = Calendar.getInstance();
 
	
	 
		
	@Override
	protected void onCreate(Bundle savedInstanceState) {
		super.onCreate(savedInstanceState);
		  setContentView(R.layout.psettings);	
	    ActionBar actbar = getActionBar();
	    actbar.setDisplayHomeAsUpEnabled(true);
	    
	    m = getIntent().getIntExtra("frommain", 3);
	    idr=getIntent().getIntExtra("idr", 3);
	    cbox=(CheckBox)findViewById(R.id.checkBox1);
	   
	     namee = (EditText)findViewById(R.id.name);
	     numbere = (EditText)findViewById(R.id.number);
	     messagee=(EditText)findViewById(R.id.message);
	     evente = (EditText)findViewById(R.id.event);
	     ringtonee = (TextView)findViewById(R.id.rtview);
	     timee = (TimePicker)findViewById(R.id.timePicker1);
	     pic=(DatePicker)findViewById(R.id.datePicker1);
	     rp = (Button)findViewById(R.id.ringpick);
	     cp = (Button)findViewById(R.id.numberpick);	
		//inflating defaults
	    
		 if(setset.defaultringtone == null ){
			  Toast.makeText(this, "select default ringtone in settings", Toast.LENGTH_SHORT).show();
		  startActivity(new Intent(this,setset.class));}
		  else{ringtone=setset.defaultringtone.toString();
		 ainsmode=setset.dainsmodes;
		 timehour=setset.dhour;
		 timeminute=setset.dminute;}
		
		 ringtonee.setText(ringtone);
		 if(ainsmode==1){cbox.setChecked(true);}
		 if(ainsmode==0){cbox.setChecked(false);}
		   timee.setCurrentHour(timehour);
			 timee.setCurrentMinute(timeminute);
			 
		  
		 		 
	     //coming to conditional inflating
	    if(m == 2){
	    	SQLiteDatabase d = db.getReadableDatabase();
	    	d.beginTransaction();
    String columns[] = {dbfile.ainsmod,dbfile.date,dbfile.month
	,dbfile.year,dbfile.message,dbfile.minute,dbfile.hour,dbfile.name,dbfile.number,dbfile.eventcategory,dbfile.ringtone};
   
    String selection = "_id="+idr.toString(); 
    Cursor q = d.query(dbfile.elist, columns, selection,null,null,null,null);
    if(q.moveToFirst()){
   
    name=q.getString(q.getColumnIndexOrThrow(dbfile.name));
   number=q.getString(q.getColumnIndexOrThrow(dbfile.number));
   message=q.getString(q.getColumnIndexOrThrow(dbfile.message));
   ainsmode=q.getInt(q.getColumnIndexOrThrow(dbfile.ainsmod));
   date=q.getInt(q.getColumnIndexOrThrow(dbfile.date));
  month=q.getInt(q.getColumnIndexOrThrow(dbfile.month));
  timehour=q.getInt(q.getColumnIndexOrThrow(dbfile.hour)); 
  timeminute=q.getInt(q.getColumnIndexOrThrow(dbfile.minute));
  year=q.getInt(q.getColumnIndexOrThrow(dbfile.year));
   ringtone=q.getString(q.getColumnIndexOrThrow(dbfile.ringtone));
   event=q.getString(q.getColumnIndexOrThrow(dbfile.eventcategory));
  
    }
    q.close();d.setTransactionSuccessful();
	d.endTransaction();d.close();
	namee.setText(name);
	 evente.setText(event);
	pic.init(year, month-1, date,null);
	timee.setCurrentHour(timehour);
	timee.setCurrentMinute(timeminute);
	
	
	numbere.setText(number);
	 if(ainsmode==1){cbox.setChecked(true);}
	 if(ainsmode==0){cbox.setChecked(false);}
	ringtonee.setText(ringtone);}
	  	    
	  
	    
	    rp.setOnClickListener(new View.OnClickListener() {		
			@Override
			public void onClick(View v) {
				// TODO Auto-generated method stub
				 pickring(v);
			}

			private void pickring(View v) {
				// TODO Auto-generated method stub
				startActivityForResult(new Intent(RingtoneManager.ACTION_RINGTONE_PICKER),3);
			}
		});
	    
	    //time
	    //time
	 	  
	    
	    	   
		
		
		//contactpic
		 cp.setOnClickListener(new View.OnClickListener() {
			
			@Override
			public void onClick(View v) {
				// TODO Auto-generated method stub
				 pickcontact(v);
			}

			private void pickcontact(View v) {
				Intent picking = new Intent(Intent.ACTION_PICK,ContactsContract.CommonDataKinds.Phone.CONTENT_URI);
				startActivityForResult(picking,2);
				
			}
		});
		 
		 
		 
	}
	
	@Override
    protected void onActivityResult(int request,int result,Intent data){
    	super.onActivityResult(request, result, browser);
    	switch(request){
    	case(2):if(result==RESULT_OK){super.onActivityResult(request, result, data);
    		Uri contact = data.getData();
    		Cursor c = managedQuery(contact, null, null, null, null);
    				if(c.moveToFirst())
    		{	name = c.getString(c.getColumnIndexOrThrow(ContactsContract.Contacts.DISPLAY_NAME));
    		number = c.getString(c.getColumnIndexOrThrow(ContactsContract.CommonDataKinds.Phone.NUMBER));
    		namee.setText(name);
    		numbere.setText(number);
    		c.close();}
    	   	    		    	}break;
    	   	case(3):{if(result == RESULT_OK){
      			 ringtone = (data.getParcelableExtra(RingtoneManager.EXTRA_RINGTONE_PICKED_URI)).toString();
      			ringtonee.setText(ringtone);}}
                    	   	
    	   	break;}
    
    
    }

	@Override
	public boolean onCreateOptionsMenu(Menu menu) {
		// Inflate the menu; this adds items to the action bar if it is present.
		super.onCreateOptionsMenu(menu);
				getMenuInflater().inflate(R.layout.addmenu, menu);
		return true;
	}
	
	@Override
	public boolean onOptionsItemSelected(MenuItem item) {
		// Handle action bar item clicks here. The action bar will
		// automatically handle clicks on the Home/Up button, so long
		// as you specify a parent activity in AndroidManifest.xml.
		int id = item.getItemId();
	
		if (id == R.id.m) {	
			
									
			if(m==1){
			//sending to dbfile
		
			name = namee.getText().toString().trim();
		 event = evente.getText().toString().trim();
			 message = messagee.getText().toString();
			 number = numbere.getText().toString();
			 ringtone = ringtonee.getText().toString();
			 timehour = timee.getCurrentHour();
			 timeminute = timee.getCurrentMinute();
			 if(((CheckBox)findViewById(R.id.checkBox1)).isChecked() == true)
				{ainsmode = 1;}
				else
				{ainsmode = 0;}
				  date = pic.getDayOfMonth();
				 month = pic.getMonth()+1;
				 year = pic.getYear();
				
	
	
 e= new entry(name,number,event,message,timehour,timeminute,ringtone,date,month,year,ainsmode);			
 

		if(name.equals("") == true){Toast.makeText(this,"name is required", Toast.LENGTH_SHORT).show();}
		if(event.equals("") == true){Toast.makeText(this,"event is required", Toast.LENGTH_SHORT).show();}
		
			
		
		if(name.equals("")  == false){if(event.equals("")==false){
			
			
			int lastid=db.lastid();	 
	      
			
		
		final SimpleDateFormat df = new SimpleDateFormat("MM/dd/yyyy");
	
		Calendar myc = Calendar.getInstance();
		myc.clear();
		try {
			myc.setTime(df.parse(month+"/"+date+"/"+year));
		} catch (ParseException e1) {
			// TODO Auto-generated catch block
			e1.printStackTrace();
		}
		myc.set(Calendar.HOUR_OF_DAY, timehour);
		myc.set(Calendar.MINUTE, timeminute);
		myc.set(Calendar.SECOND, 0);
		myc.set(Calendar.MILLISECOND, 0);		
		
			if(now.compareTo(myc)==1){
				Toast.makeText(this, "alarms cannot be rung in past",Toast.LENGTH_SHORT ).show();
			}if(now.compareTo(myc)== -1){
				db.entry(e);
Toast.makeText(add.this, "Alarm is set at" + myc.getTime(),Toast.LENGTH_LONG).show();
		Intent in = new Intent(this,br.class);
		in.putExtra("id", lastid);
	   in.setAction("android");
	   PendingIntent put = PendingIntent.getBroadcast(this,lastid , in, PendingIntent.FLAG_ONE_SHOT);     
	     
	      
	        AlarmManager myalarm = (AlarmManager)getSystemService(Context.ALARM_SERVICE);
	        
	        myalarm.set(AlarmManager.RTC_WAKEUP, myc.getTimeInMillis(), put);
	            
	       startActivity(new Intent(this,MainActivity.class));}
	             
	      }}    
	          	       
	                          	      
	       	     					 			
	
		}
		if(m==2){
			name = namee.getText().toString();
			 event = evente.getText().toString();
				 message = messagee.getText().toString();
				 number = (numbere.getText()).toString();
				 ringtone = (ringtonee).getText().toString();
				 timehour = (timee).getCurrentHour();
				 timeminute = (timee).getCurrentMinute();
				 if(((CheckBox)findViewById(R.id.checkBox1)).isChecked() == true)
					{ainsmode = 1;}
					else
					{ainsmode = 0;}
					  date = pic.getDayOfMonth();
					 month = pic.getMonth()+1;
					 year = pic.getYear();
					 
		e= new entry(name,number,event,message,timehour,timeminute,ringtone,date,month,year,ainsmode);			
		if(name.equals("") == true){Toast.makeText(this,"name is required", Toast.LENGTH_SHORT).show();}
		if(event.equals("") == true){Toast.makeText(this,"event is required", Toast.LENGTH_SHORT).show();}
		if(name.equals("")  == false){if(event.equals("")  == false){		
		
		final SimpleDateFormat df = new SimpleDateFormat("MM/dd/yyyy");
		
		Calendar mc = Calendar.getInstance();
		mc.clear();
		try {
			mc.setTime(df.parse(month+"/"+date+"/"+year));
		} catch (ParseException e1) {
			// TODO Auto-generated catch block
			e1.printStackTrace();
		}	
		mc.set(Calendar.HOUR_OF_DAY, timehour);
		mc.set(Calendar.MINUTE, timeminute);
		mc.set(Calendar.SECOND, 0);
		mc.set(Calendar.MILLISECOND, 0);		
		
		
			
			
		Intent in = new Intent(this,br.class);
		in.setAction("android");
		in.putExtra("id", idr);
	if(now.compareTo(mc)==1){
		Toast.makeText(this, "alarms cannot be rung in past",Toast.LENGTH_SHORT ).show();
	}
	if(now.compareTo(mc)== -1){db.onchangevalues(e,idr);
		Toast.makeText(add.this, "Alarm is set at" + mc.getTime(),Toast.LENGTH_LONG).show();
		PendingIntent t = PendingIntent.getBroadcast(this, idr, in, PendingIntent.FLAG_ONE_SHOT);    
	   AlarmManager malarm = (AlarmManager)getSystemService(Context.ALARM_SERVICE);
	       malarm.cancel(t);
	       malarm.set(AlarmManager.RTC_WAKEUP, mc.getTimeInMillis(), t);
	 
	       startActivity(new Intent(this,MainActivity.class));}
							
			}		 }
						
		}
		return true;
		}  
		if(id == android.R.id.home){
		startActivity(new Intent(this,MainActivity.class));
				return true;
		}
				else return false;
		
	}

}
