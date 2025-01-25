#! /usr/bin/env python3
try:
    import requests, re, os, time, json
    from requests.exceptions import RequestException
    from rich import print as Println
    from rich.panel import Panel
    from rich.console import Console
except Exception as error:
    exit(f"[Error] {str(error).capitalize()}!")

SUKSES, GAGAL = (
    [],
    [],
)

def BANNER() -> None:
    os.system('cls' if os.name == 'nt' else 'clear')
    Println(
        Panel(r"""[bold red]●[bold yellow] ●[bold green] ●[/]
[bold red]    ________  .____    ._______________________
    \_____  \ |    |   |   \____    /\____    /
     /  / \  \|    |   |   | /     /   /     / 
    /   \_/.  \    |___|   |/     /_  /     /_ 
[bold white]    \_____\ \_/_______ \___/_______ \/_______ \
           \__>       \/           \/        \/
        [underline green]Instagram Qlizz - Coded by Rozhak-XD""", width=55, style="bold bright_white")
    )
    return

class CHECKING:

    def __init__(self) -> None:
        pass

    def LOGIN(self) -> None:
        try:
            BANNER()
            Println(Panel(f"[bold white]Silakan Masukkan Cookies Qlizz, Pastikan Akun Sudah Dalam Keadaan Login!", width=55, style="bold bright_white", subtitle="[bold bright_white]╭─────", subtitle_align="left", title="[bold bright_white]>> [Login Cookies] <<"))
            cookies = Console().input("[bold bright_white]   ╰─> ")
            self.status = self.VALIDATION(cookies, status_token=False)
            if str(self.status) == "Login Sukses":
                with open('Penyimpanan/Cookie.json', 'w') as w:
                    w.write(json.dumps({
                        "Cookie": f"{cookies}"
                    }, indent=4))
                Println("[bold bright_white]   ──>[bold green] LOGIN BERHASIL...")
                time.sleep(2.5)
                
            else:
                Println(Panel("[bold red]Maaf, Cookies Yang Anda Masukkan Tidak Valid, Silak\nan Coba Untuk Mengambil Ulang Cookies!", width=55, style="bold bright_white", title="[bold bright_white]>> [Login Error] <<"))
                exit()
        except Exception as error:
            Println(Panel(f"[bold red]{str(error).title()}!", width=55, style="bold bright_white", title="[bold bright_white]>> [Error] <<"))
            exit()

    def VALIDATION(self, cookies: str, status_token: bool = False) -> str:
        with requests.Session() as session:
            session.headers.update(
                {
                    'Host': 'buyinstafollowers.xyz',
                    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                    'sec-fetch-site': 'none',
                    'accept-language': 'en-US,en;q=0.9',
                    'sec-fetch-mode': 'navigate',
                    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
                    'sec-fetch-user': '?1',
                    'sec-fetch-dest': 'document',
                }
            )
            response = session.get('https://buyinstafollowers.xyz/', cookies = {
                'cookie': cookies
            })
            if 'href="/instagram/logout"' in response.text and 'Hello ' in response.text:
                if bool(status_token) == True:
                    self._token = re.search('type="hidden" name="_token" value="(.*?)"', response.text).group(1)
                    return self._token
                else:
                    return "Login Sukses"
            else:
                return "Login Gagal"

def FEATURES() -> None:
    try:
        BANNER()
        cookies = json.loads(open('Penyimpanan/Cookie.json', 'r').read())['Cookie']
        status = CHECKING().VALIDATION(cookies, status_token=False)
        if str(status) != "Login Sukses":
            Println(Panel("[bold red]Maaf, Cookies Yang Anda Masukkan Tidak Valid, Silak\nan Coba Untuk Mengambil Ulang Cookies!", width=55, style="bold bright_white", title="[bold bright_white]>> [Login Error] <<"))
            time.sleep(5.0)
            CHECKING().LOGIN()
        else:
            pass
    except Exception as error:
        Println(Panel(f"[bold red]{str(error).title()}!", width=55, style="bold bright_white", title="[bold bright_white]>> [Error] <<"))
        time.sleep(5.0)
        CHECKING().LOGIN()

    Println(Panel(f"[bold white]Silahkan Masukan Username Akun Instagram Dan Pastik\nan Akun Tersebut Tidak Terkunci!", width=55, style="bold bright_white", subtitle="[bold bright_white]╭─────", subtitle_align="left", title="[bold bright_white]>> [Your Username] <<"))
    username = Console().input("[bold bright_white]   ╰─> ")
    if len(username) > 3:
        Println(Panel("[bold white]Anda Bisa Menggunakan[bold yellow] CTRL + C[bold white] Jika Stuck Dan Gunak\nan[bold red] CTRL + Z[bold white] Untuk Berhenti!", width=55, style="bold bright_white", title="[bold bright_white]>> [Notes] <<"))
        try:
            while True:
                try:
                    SUBMIT().FOLLOWERS(cookies, username)
                except KeyboardInterrupt:
                    Println("\r                                              ", end='\r')
                    time.sleep(1.5)
                    continue
                except RequestException:
                    Println("[bold bright_white]   ──>[bold red] KONEKSI ERROR...                          ", end='\r')
                    time.sleep(10.0)
                    continue
        except Exception as error:
            Println(Panel(f"[bold red]{str(error).title()}!", width=55, style="bold bright_white", title="[bold bright_white]>> [Error] <<"))
            exit()
    else:
        Println(Panel("[bold red]Maaf, Username Yang Anda Masukkan Terlalu Pendek, Silahkan Masukkan Username Yang Valid!", width=55, style="bold bright_white", title="[bold bright_white]>> [Wrong Username] <<"))
        exit()

class SUBMIT:

    def __init__(self) -> None:
        pass

    def FOLLOWERS(self, cookies: str, username: str) -> bool:
        with requests.Session() as session:
            self._token = CHECKING().VALIDATION(cookies, status_token=True)
            session.headers.update(
                {
                    'origin': 'https://buyinstafollowers.xyz',
                    'Host': 'buyinstafollowers.xyz',
                    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
                    'referer': 'https://buyinstafollowers.xyz/',
                    'sec-fetch-site': 'same-origin',
                    'accept': '*/*',
                    'accept-language': 'en-US,en;q=0.9',
                    'sec-fetch-mode': 'cors',
                    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
                    'sec-fetch-dest': 'empty',
                }
            )
            data = {
                '_token': self._token,
                'tool': '/',
                'link': username,
            }
            response = session.post('https://buyinstafollowers.xyz/instagram/send', data = data, cookies = {
                'cookie': cookies
            })
            if 'Your post is successfully added for free' in response.text:
                SUKSES.append(response.text)
                self.followers_count = re.search('free (.*?) followers.', response.text)
                self.followers_count = self.followers_count.group(1) if self.followers_count else "10"
                Println(Panel(f"""[bold white]Username :[bold green] @{username}
[bold white]Link :[bold red] https://www.instagram.com/{username[:18]}
[bold white]Jumlah :[bold green] +{self.followers_count}""", width=55, style="bold bright_white", title="[bold bright_white]>> [Success] <<"))
                return True
            elif 'free submit will be available after' in response.text:
                self.total_delay = re.search('after (.*?) minutes. ', response.text).group(1)
                Println(f"[bold bright_white]   ──>[bold green] HARAP TUNGGU {self.total_delay} MENIT...                      ", end='\r')
                for detik in range(int(self.total_delay) * 60, 0, -1):
                    Println(f"[bold bright_white]   ──>[bold green] {detik}[bold white]/[bold blue]@{username}[bold white] SUKSES:-[bold green]{len(SUKSES)}[bold white] GAGAL:-[bold red]{len(GAGAL)}[bold white]         ", end='\r')
                    time.sleep(1)
                return False
            else:
                GAGAL.append(response.text)
                Println("[bold bright_white]   ──>[bold red] GAGAL MENGIRIMKAN PENGIKUT...               ", end='\r')
                return False

if __name__ == '__main__':
    try:
        os.system("git pull")
        if not os.path.exists("Penyimpanan/Subscribe.json"):
            youtube_link = json.loads(requests.get('https://raw.githubusercontent.com/RozhakXD/Qlizz/refs/heads/main/Penyimpanan/Youtube.json').text)['Link']
            os.system(f'xdg-open {youtube_link}')
            with open('Penyimpanan/Subscribe.json', 'w') as w:
                w.write(json.dumps({"Status": True}, indent=4))
            time.sleep(5.0)
        FEATURES()
    except KeyboardInterrupt:
        exit()