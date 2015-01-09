package com.example.eventremainder;

import java.util.Calendar;

import android.app.Activity;
import android.app.AlarmManager;
import android.app.KeyguardManager;
import android.app.KeyguardManager.KeyguardLock;
import android.app.PendingIntent;
import android.content.Context;
import android.content.Intent;
import android.media.AudioManager;
import android.media.Ringtone;
import android.media.RingtoneManager;
import android.net.Uri;
import android.os.Bundle;
import android.os.PowerManager;
import android.view.View;
import android.view.Window;
import android.view.WindowManager;
import android.widget.Button;
import android.widget.TextView;
import android.widget.Toast;

public class dc extends Activity{PowerManager pm;
PowerManager.WakeLock wl;
	static Ringtone ring = null;int h;Context co = this;int i;
	String	contactpic = null;int ye;dbfile kol = new dbfile(this);

	AudioManager am;int date,month,hour,minute;PendingIntent hoi;
	
	KeyguardLock keyguardLock;
	
	
	@Override
	protected void onCreate(Bundle savedInstanceState) {
		super.onCreate(savedInstanceState);
		Window win = getWindow();
	System.out.println("oncreate");
		win.setFlags(WindowManager.LayoutParams.FLAG_FULLSCREEN | 
			    WindowManager.LayoutParams.FLAG_DISMISS_KEYGUARD | 
			    WindowManager.LayoutParams.FLAG_SHOW_WHEN_LOCKED | 
			    WindowManager.LayoutParams.FLAG_TURN_SCREEN_ON,
			    WindowManager.LayoutParams.FLAG_FULLSCREEN | 
			    WindowManager.LayoutParams.FLAG_DISMISS_KEYGUARD | 
			    WindowManager.LayoutParams.FLAG_SHOW_WHEN_LOCKED | 
			    WindowManager.LayoutParams.FLAG_TURN_SCREEN_ON|
			    WindowManager.LayoutParams.FLAG_KEEP_SCREEN_ON);
		setContentView(R.layout.dialog);
	
		  h = this.getIntent().getIntExtra("id",-1);
		  System.out.println(h);
		String myname = kol.thename(h);
		String myevent = kol.theevent(h);
		 month = kol.themonth(h);
		 date =kol.thedate(h);
		 hour = kol.thehour(h);
		 minute = kol.theminute(h);
		ye = kol.theyear(h); 
		pm = (PowerManager)getSystemService(Context.POWER_SERVICE);
		wl = pm.newWakeLock(PowerManager.FULL_WAKE_LOCK, "My Tag");
	
		if(pm.isScreenOn()==false){
		
		 wl.acquire();
		 
		 
		 KeyguardManager keyguardManager = (KeyguardManager) getApplicationContext().getSystemService(Context.KEYGUARD_SERVICE); 
        keyguardLock =  keyguardManager.newKeyguardLock("TAG");
         keyguardLock.disableKeyguard();
		    
              
		}  
 
		
		 Intent in = new Intent(this,br.class);
		in.putExtra("id", h);
		in.setAction("android");
		 hoi = PendingIntent.getBroadcast(this, h, in, PendingIntent.FLAG_ONE_SHOT);
		final String msgreq = kol.themessage(h);
		final String reqnum = kol.thenumber(h);		
		int ainsmod = kol.theains(h);
		String Ringtone = kol.ther(h);
	String p = myname+"'s" + myevent;
 am = (AudioManager)getSystemService(Context.AUDIO_SERVICE);    
 i=am.getStreamVolume(AudioManager.STREAM_RING);
     ring = RingtoneManager.getRingtone(this, Uri.parse(Ringtone));	
	int t = am.getRingerMode();

	if(ainsmod==1)
	   {
	   am.setStreamVolume(AudioManager.STREAM_RING, setset.volumes, AudioManager.FLAG_PLAY_SOUND);
	  ring.play();System.out.println("a");}
	if(ainsmod==0){{if(t==AudioManager.RINGER_MODE_NORMAL){
		am.setStreamVolume(AudioManager.STREAM_RING, setset.volumes, AudioManager.FLAG_PLAY_SOUND);
		ring.play();System.out.println("b");}}}

	
	Button stop = (Button)findViewById(R.id.butto1);
	Button call = (Button)findViewById(R.id.butto2);
	Button msg = (Button)findViewById(R.id.butto3);
	
	((TextView)findViewById(R.id.textVie1)).setText(p);
	
	stop.setOnClickListener(new View.OnClickListener() {
		
		@Override
		public void onClick(View v) {if(ring.isPlaying()){ring.stop();
		am.setStreamVolume(AudioManager.STREAM_RING, i, AudioManager.FLAG_PLAY_SOUND);}
			// TODO Auto-generated method stub
	kol.upyear(ye);
	
	AlarmManager myalarm = (AlarmManager)getSystemService(Context.ALARM_SERVICE);
	Calendar c = Calendar.getInstance();
	c.set(Calendar.DATE, date);
	c.set(Calendar.YEAR, ye+1);
	c.set(Calendar.MONTH, month);
	c.set(Calendar.MINUTE, minute);
	c.set(Calendar.HOUR,hour);
	myalarm.set(AlarmManager.RTC_WAKEUP, c.getTimeInMillis(), hoi);
	c.clear();
	finish();
		}
	});
	
call.setOnClickListener(new View.OnClickListener() {
		
		@Override
		public void onClick(View v) {
			
			if(ring.isPlaying())
			{ring.stop();
			 am.setStreamVolume(AudioManager.STREAM_RING, i, AudioManager.FLAG_PLAY_SOUND);}
			
			
			
			kol.upyear(ye);
			
			
			
			
			AlarmManager myalarm = (AlarmManager)getSystemService(Context.ALARM_SERVICE);
			Calendar c = Calendar.getInstance();
			c.set(Calendar.DATE, date);
			c.set(Calendar.YEAR, ye+1);
			c.set(Calendar.MONTH, month);
			c.set(Calendar.MINUTE, minute);
			c.set(Calendar.HOUR,hour);
			myalarm.set(AlarmManager.RTC_WAKEUP, c.getTimeInMillis(), hoi);
			c.clear();
		
		
			Intent i = new Intent(Intent.ACTION_DIAL,Uri.parse("tel:"+reqnum));
			
			startActivity(i);
		}
	});

   msg.setOnClickListener(new View.OnClickListener() {
	
	@Override
	public void onClick(View v) {
		// TODO Auto-generated method stub
		if(ring.isPlaying())
		{ring.stop();
		am.setStreamVolume(AudioManager.STREAM_RING, i, AudioManager.FLAG_PLAY_SOUND);}
		
		kol.upyear(ye);
		
		
		
		AlarmManager myalarm = (AlarmManager)getSystemService(Context.ALARM_SERVICE);
		Calendar c = Calendar.getInstance();
		c.set(Calendar.DATE, date);
		c.set(Calendar.YEAR, ye+1);
		c.set(Calendar.MONTH, month);
		c.set(Calendar.MINUTE, minute);
		c.set(Calendar.HOUR,hour);
		myalarm.set(AlarmManager.RTC_WAKEUP, c.getTimeInMillis(), hoi);
		c.clear();
		
		
		
		if(msgreq!=null){if(reqnum!=null){
		Uri smsUri = Uri.parse("tel:"+reqnum);
		Intent intent = new Intent(Intent.ACTION_VIEW, smsUri);
		intent.putExtra("sms_body", msgreq);
		intent.setType("vnd.android-dir/mms-sms");
		startActivity(intent);}
	}if(msgreq==null){Toast.makeText(getApplicationContext(), "msg not given",Toast.LENGTH_SHORT).show();}
	if(reqnum == null){Toast.makeText(getApplicationContext(), "no number given",Toast.LENGTH_SHORT).show();}}
	
   });
	}
    




@Override
protected void onPause(){
	super.onPause();System.out.println("onpause");
	if(ring.isPlaying()){ring.stop();
	am.setStreamVolume(AudioManager.STREAM_RING, i, AudioManager.FLAG_PLAY_SOUND);}
	


boolean yuio = wl.isHeld();

if(yuio==true){
wl.release();Bundle b = null;
onCreate(b);keyguardLock.reenableKeyguard();}
if(yuio==false){
	kol.upyear(ye);
AlarmManager myalarm = (AlarmManager)getSystemService(Context.ALARM_SERVICE);
Calendar c = Calendar.getInstance();
c.set(Calendar.DATE, date);
c.set(Calendar.YEAR, ye+1);
c.set(Calendar.MONTH, month);
c.set(Calendar.MINUTE, minute);
c.set(Calendar.HOUR,hour);

myalarm.set(AlarmManager.RTC_WAKEUP, c.getTimeInMillis(), hoi);
c.clear();

	finish();}
}

@Override
public  void onResume(){
	super.onResume();
}
}




