package com.example.eventremainder;

import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.util.Calendar;

import android.app.AlarmManager;
import android.app.PendingIntent;
import android.content.BroadcastReceiver;
import android.content.Context;
import android.content.Intent;
import android.os.Bundle;
import android.widget.Toast;

public class br extends BroadcastReceiver{


	@Override
	public void onReceive(Context context, Intent intent) {
		// TODO Auto-generated method stub
		dbfile dgs = new dbfile(context);
	SimpleDateFormat df = new SimpleDateFormat("MM/dd/yyyy");
		
		if(intent.getAction()=="android"){
		Bundle extras = intent.getExtras();
		int i = extras.getInt("id", 100);
		Intent f = new Intent(context,dc.class);
		f.setFlags(Intent.FLAG_ACTIVITY_NEW_TASK);
		f.putExtra("id", i);
		context.startActivity(f);}
		
		
		
		if(intent.getAction()=="android.intent.action.BOOT_COMPLETED"){
			int yu = dgs.lastid();int x;
			for(x = 1 ; x < (yu+1);x=(x+1)){
				Calendar c = Calendar.getInstance();
				int year = dgs.theyear(x);
				int month = dgs.themonth(x);
				int date = dgs.thedate(x);
				int hour = dgs.thehour(x);
				int minute = dgs.theminute(x);
				
				try {
					c.setTime(df.parse(month+"/"+date+"/"+year));
				} catch (ParseException e1) {
					// TODO Auto-generated catch block
					e1.printStackTrace();
				}
				
				
				c.set(Calendar.MINUTE, minute);
				c.set(Calendar.HOUR,hour);
				c.set(Calendar.SECOND, 0);
				c.set(Calendar.MILLISECOND, 0);	
				Intent in = new Intent(context,dc.class);
				in.putExtra("id", x);
				PendingIntent po = PendingIntent.getBroadcast(context,x ,in , PendingIntent.FLAG_ONE_SHOT);
				 AlarmManager asa = (AlarmManager)context.getSystemService(Context.ALARM_SERVICE);
				asa.set(AlarmManager.RTC_WAKEUP, c.getTimeInMillis(),po );			
			c.clear();
			}
			
		}
	}

}
