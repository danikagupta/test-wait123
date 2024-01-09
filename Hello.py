import streamlit as st
import time

st.title("UI for waiting!!")

msg_id=0

def show_message(start_time,end_time,t,msgs):
  global msg_id
  time_taken=round(time.time()-start_time)
  if(time.time()>end_time):
    msg=f"## Processing took {time_taken} seconds"
    return msg
  msg=msgs[time_taken//t % len(msgs)]
  ts=time.strftime("%H:%M:%S", time.localtime())
  tf=f"0:{time_taken}"
  if(time_taken<10):
    tf=f"0:0{time_taken}"
  if(time_taken>=60):
    mins=time_taken//60
    secs=time_taken-mins*60
    tf=f"{mins}:{secs}"
  return f"## {ts} \n## {tf}\n## {msg}"

def runFor(tot,t,msgs):
  start_time = time.time()
  end_time=time.time()+tot

  while True:
    print(f"In the loop at {time.time()} with start at {start_time} and end at {end_time}")
    with st.spinner(show_message(start_time,end_time,t,msgs)):
      time.sleep(t)
    if(time.time()>end_time):
      st.write(show_message(start_time,end_time,t,msgs))
      break;


runFor(15,1,["ABC","DEF","GHI","JKL"])