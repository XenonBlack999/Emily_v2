try:
    import speedtest
except ImportError:
    print("Error: speedtest module not found. Please install with 'pip install speedtest-cli'")

from emily_v2 import speak  

def test_speedtest_setup():
    try:
        st = speedtest.Speedtest()
        best_server = st.get_best_server()
        msg = f"Connected to {best_server['host']} located in {best_server['country']}."
        print(msg)
        speak(msg)   
        return True
    except Exception as e:
        msg = f"Error during speedtest setup: {e}"
        print(msg)
        speak(msg)   
        return False


def check_internet_speed():
    st = speedtest.Speedtest()
    st.get_best_server()

    download_speed = st.download() / 1_000_000  
    upload_speed = st.upload() / 1_000_000      

    result = {
        'download_speed_mbps': round(download_speed, 2),
        'upload_speed_mbps': round(upload_speed, 2)
    }

    msg = f"Download: {result['download_speed_mbps']} Mbps, Upload: {result['upload_speed_mbps']} Mbps"
    print(msg)
    speak(msg)   
    return result
