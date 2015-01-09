package com.example.eventremainder;

import android.app.ActionBar;
import android.app.Activity;
import android.content.Context;
import android.content.Intent;
import android.content.SharedPreferences;
import android.media.AudioManager;
import android.media.RingtoneManager;
import android.net.Uri;
import android.os.Bundle;


import android.view.Menu;
import android.view.MenuItem;
import android.view.View;
import android.view.View.OnClickListener;
import android.widget.Button;
import android.widget.CompoundButton;
import android.widget.SeekBar;
import android.widget.Switch;
import android.widget.TimePicker;
import android.widget.SeekBar.OnSeekBarChangeListener;
import android.widget.Toast;


public class setset extends Activity {
Context thcom = this;public static Uri defaultringtone =null;
static int avol=0;
static int dhour=0;
static int dminute=0;	static int dainsmodes=10;static int volumes=0;
 
	@Override
	protected void onCreate(Bundle savedInstanceState) {
		super.onCreate(savedInstanceState);
	setContentView(R.layout.setset);	
	ActionBar actbar = getActionBar();
	actbar.setDisplayHomeAsUpEnabled(true);
	SharedPreferences pre = getSharedPreferences("sharedpre", Context.MODE_PRIVATE);
	 if(pre.contains("avol")){volumes=pre.getInt("avol", 1000);}
	  if(pre.contains("dhour")){dhour=pre.getInt("dhour", 1000);}
	  if(pre.contains("dminute")){dminute=pre.getInt("dminute", 1000);
	  if(pre.contains("ringingtone")){defaultringtone=Uri.parse(pre.getString("ringingtone", ""));
	  if(pre.contains("dainsmodes")){dainsmodes=pre.getInt("dainsmodes", 1000);}}}

	//ringtone
	//ringtone
	Button b1 = (Button)findViewById(R.id.ringbutton1);
	b1.setOnClickListener(new View.OnClickListener() {
		@Override
		public void onClick(View v) {System.out.println("this is it");
			startActivityForResult(new Intent(RingtoneManager.ACTION_RINGTONE_PICKER),1);
		}
	});
	
	//seekbar
	//seekbar
	SeekBar volume = (SeekBar)findViewById(R.id.seekBar1);
	final AudioManager r = (AudioManager)getSystemService(Context.AUDIO_SERVICE); 
	avol = r.getStreamMaxVolume(AudioManager.STREAM_ALARM);
	volume.setMax(avol);
	
	volume.setProgress(volumes);
	volume.setOnSeekBarChangeListener(new OnSeekBarChangeListener(){
		@Override
		public void onProgressChanged(SeekBar seekBar, int progress,boolean fromUser){
			volumes=progress;
			 
		}
		@Override
		public void onStartTrackingTouch(SeekBar seekBar) {
		// TODO Auto-generated method stub	
}
		@Override
		public void onStopTrackingTouch(SeekBar seekBar) {
			// TODO Auto-generated method stub
		
		}
			});
	
	
	final Switch swit = (Switch)findViewById(R.id.switch1);
	if(dainsmodes==1){swit.setChecked(true);}
	if(dainsmodes==0){swit.setChecked(false);}
	//time
	//time
	((TimePicker)findViewById(R.id.timePicker2)).setCurrentHour(dhour);
	((TimePicker)findViewById(R.id.timePicker2)).setCurrentMinute(dminute);
  swit.setOnCheckedChangeListener(new CompoundButton.OnCheckedChangeListener() {
	
	@Override
	public void onCheckedChanged(CompoundButton buttonView, boolean isChecked) {
		// TODO Auto-generated method stub
	if(isChecked == true){dainsmodes=1;}
	if(isChecked==false){dainsmodes=0;}
	}
});
  ((TimePicker)findViewById(R.id.timePicker2)).setCurrentHour(dhour);
  ((TimePicker)findViewById(R.id.timePicker2)).setCurrentMinute(dminute);
	Button save = (Button)findViewById(R.id.save);
	save.setOnClickListener(new OnClickListener(){

		@Override
		public void onClick(View v) {	
			dhour = ((TimePicker)findViewById(R.id.timePicker2)).getCurrentHour();
			dminute = ((TimePicker)findViewById(R.id.timePicker2)).getCurrentMinute();
			
			
			
			SharedPreferences pre = getSharedPreferences("sharedpre",Context.MODE_PRIVATE);
			SharedPreferences.Editor edit = pre.edit();
			// TODO Auto-generated method stub
			edit.putInt("avol", volumes);
			edit.putInt("dhour", dhour);
			edit.putInt("dminute",dminute);System.out.println("this is it");
			edit.putString("ringingtone",defaultringtone.toString());
			edit.putInt("dainsmodes", dainsmodes);
			edit.apply();
			if(defaultringtone==null){Toast.makeText(thcom, "pick a ringtone", Toast.LENGTH_SHORT).show();}
			else{Intent intee = new Intent(thcom,add.class);
			intee.putExtra("frommain", 1);
				startActivity(intee);}
		
		
		}});	
	}
	@Override
	protected void onActivityResult(int r,int re,Intent d){
		switch(r){case(1):{if(re == RESULT_OK){System.out.println("this is it");
			 defaultringtone = d.getParcelableExtra(RingtoneManager.EXTRA_RINGTONE_PICKED_URI);}}	
	
		}
		
	}
	

	

	@Override
	public boolean onCreateOptionsMenu(Menu menu) {
		// Inflate the menu; this adds items to the action bar if it is present.
		super.onCreateOptionsMenu(menu);				
		return true;
	}
	
	@Override
	public boolean onOptionsItemSelected(MenuItem item) {
		// Handle action bar item clicks here. The action bar will
		// automatically handle clicks on the Home/Up button, so long
		// as you specify a parent activity in AndroidManifest.xml.
		int id = item.getItemId();
	
	if(id == android.R.id.home){
		startActivity(new Intent(this,MainActivity.class));
				return true;
		}
				else return false;
		
	}




}
