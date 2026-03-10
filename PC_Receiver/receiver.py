import http.server
import socketserver
import os
import sys
import socket
import datetime

PORT = 8000

def get_local_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(('10.255.255.255', 1))
        ip = s.getsockname()[0]
    except Exception:
        ip = '127.0.0.1'
    finally:
        s.close()
    return ip

class FileReceiverHandler(http.server.SimpleHTTPRequestHandler):
    
    def setup(self):
        super().setup()
        self.request.settimeout(5.0) 

    def do_POST(self):
        filename = self.headers.get('File-Name', 'file.dat')
        content_length = int(self.headers.get('Content-Length', 0))
        
        today_date = datetime.datetime.now().strftime("%Y-%m-%d")
        save_dir = os.path.join(os.getcwd(), "Lumia_Transfers", today_date)
        os.makedirs(save_dir, exist_ok=True) 
        
        full_save_path = os.path.join(save_dir, filename)
        
        print(f"\n📥 Incoming: {filename}")
        
        transfer_complete = False

        try:
            with open(full_save_path, "wb") as f:
                remaining = content_length
                while remaining > 0:
                    chunk_size = min(remaining, 1024 * 1024) 
                    chunk = self.rfile.read(chunk_size)
                        
                    if not chunk: 
                        break
                        
                    f.write(chunk)
                    remaining -= len(chunk)
                    
                    done = content_length - remaining
                    percent = int(done * 100 / content_length) if content_length > 0 else 100
                    bar_length = 30
                    filled_length = int(bar_length * percent // 100)
                    bar = '█' * filled_length + '-' * (bar_length - filled_length)
                    
                    sys.stdout.write(f"\r|{bar}| {percent}% ({done // (1024*1024)} MB / {content_length // (1024*1024)} MB)")
                    sys.stdout.flush()
            
            if remaining == 0:
                transfer_complete = True
                print(f"\n✅ Saved to: {full_save_path}")
                self.send_response(200)
                self.end_headers()
            else:
                print("\n⚠️ Transfer stopped early by phone.")
                
        except ConnectionResetError:
            print("\n⚠️ Transfer cleanly aborted by phone. Ready for next file.")
        except socket.timeout:
            print("\n⚠️ Connection timed out. Ready for next file.")
        except Exception as e:
            # Intercept the ugly WinError 10054
            if "10054" in str(e):
                print("\n⚠️ Transfer cleanly aborted by phone. Ready for next file.")
            else:
                print(f"\n❌ Unexpected error: {e}")
            
        finally:
            if not transfer_complete and os.path.exists(full_save_path):
                try:
                    os.remove(full_save_path)
                except:
                    pass

    # This completely silences the messy background HTTP logs!
    def log_message(self, format, *args):
        pass

local_ip = get_local_ip()

try:
    with socketserver.TCPServer(("", PORT), FileReceiverHandler) as httpd:
        print(f"\n🚀 LUMIA SEND: TWO-WAY BRIDGE ACTIVE")
        print(f"👉 TYPE THIS INTO YOUR APP:")
        print(f"   IP:   {local_ip}")
        print(f"   Port: {PORT}")
        print("\nWaiting for connections... (Press Ctrl+C to shut down)")
        httpd.serve_forever()
except KeyboardInterrupt:
    print("\n\n🛑 Server stopped by user.")
    sys.exit(0)