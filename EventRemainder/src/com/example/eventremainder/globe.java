package com.example.eventremainder;

import android.app.Application;
import android.content.Context;
import android.content.SharedPreferences;
import android.net.Uri;

public class globe extends Application{
@Override
public void onCreate(){
	SharedPreferences pre = getSharedPreferences("sharedpre", Context.MODE_PRIVATE);
	 if(pre.contains("avol")){setset.volumes=pre.getInt("avol", 1000);}
	  if(pre.contains("dhour")){setset.dhour=pre.getInt("dhour", 1000);}
	  if(pre.contains("dminute")){setset.dminute=pre.getInt("dminute", 1000);
	  if(pre.contains("ringingtone")){setset.defaultringtone=Uri.parse(pre.getString("ringingtone", ""));
	  if(pre.contains("dainsmodes")){setset.dainsmodes=pre.getInt("dainsmodes", 1000);}}}
}
}
