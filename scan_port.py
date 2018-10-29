import _thread, time, socket


class Scan_Ip():
    def sock_port(self, ip, port):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            result = sock.connect_ex((ip, port))
            if result == 0:
                lock = _thread.allocate_lock()
                lock.acquire()
                print(f"{ip}：{port},已经被占用")
                lock.release()
        except:
            print("扫描异常")

    def ip_scan(self, ip):
        # 输入ip,扫描IP的0-65534端口情况
        try:
            print("开始扫描")
            start_time = time.time()
            for i in range(65):
                _thread.start_new_thread(self.sock_port, (ip, int(i)))
            print(f"扫描结束，共用时间：{time.time()-start_time}")

        except Exception as e:
            print(f"出现错误:{e}")
        finally:
            print("扫描结束")

if __name__ == '__main__':
    A = Scan_Ip()
    A.ip_scan("192.168.3.199")