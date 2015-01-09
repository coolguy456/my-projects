package com.example.eventremainder;

import android.app.Activity;
import android.app.ListActivity;
import android.content.Context;
import android.content.Intent;
import android.net.Uri;
import android.os.Bundle;
import android.view.Menu;
import android.view.MenuItem;

public class MainActivity extends Activity {
	
	public String shared = "shared";
Context co = this;String kumar; String kumaar;

	@Override
	protected void onCreate(Bundle savedInstanceState) {
		super.onCreate(savedInstanceState);
		setContentView(R.layout.activity_main);
		  	
		 }
	

	


		@Override
	public boolean onCreateOptionsMenu(Menu menu) {
		// Inflate the menu; this adds items to the action bar if it is present.
		super.onCreateOptionsMenu(menu);
				getMenuInflater().inflate(R.layout.menumain, menu);
		return true;
	}

	@Override
	public boolean onOptionsItemSelected(MenuItem item) {
		// Handle action bar item clicks here. The action bar will
		// automatically handle clicks on the Home/Up button, so long
		// as you specify a parent activity in AndroidManifest.xml.
		int id = item.getItemId();
		if (id == R.id.add) {Intent b = new Intent(this,add.class);
		b.putExtra("frommain", 1);
			startActivity(b);
			return true;
		}
		if(id == R.id.support){
		startActivity(new Intent(Intent.ACTION_VIEW,Uri.parse("https://www.youtube.com")));
			return true;
		}
		if(id == R.id.settings){
			startActivity(new Intent(this,setset.class));
			return true;
		}
		
		else return false;
	}
	
	
	
}
