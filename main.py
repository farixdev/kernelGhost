import time
import random
import sys
from colorama import Fore, Style, init

init(autoreset=True)
import os

import sys

# Works on most terminals (Linux, macOS, Windows 10+ with ANSI support)
sys.stdout.write("\33Command Prompt\a")
sys.stdout.flush()


# ========== Fake Progress Bar ==========
def progress_bar(task, duration=30, length=40):
    steps = 50
    interval = duration / steps
    for i in range(steps + 1):
        percent = int((i / steps) * 100)
        bar = "█" * int(length * i / steps) + "-" * (length - int(length * i / steps))
        sys.stdout.write(f"\r{Fore.WHITE}{task} |{bar}| {percent}%")
        sys.stdout.flush()
        time.sleep(interval)
    print("\n")


def random_progress(task, package=None):
    choice = random.choice(["generic", "pip", "wget", "apt"])

    if choice == "pip" and package:
        pip_style_progress(package, size_mb=random.randint(5, 20))
    elif choice == "wget" and package:
        wget_style_progress(package + ".tar.gz", size_mb=random.randint(10, 40))
    elif choice == "apt" and package:
        apt_style_progress(package, size_kb=random.randint(500, 3000))
    else:
        progress_bar(task, duration=random.randint(5, 12))


def wget_style_progress(file, size_mb=40):
    url = f"https://example.com/{file}"
    ip = "93.184.216.34"
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")

    print(f"--{timestamp}--  {url}")
    time.sleep(0.5)
    print(f"Resolving example.com... {ip}")
    time.sleep(0.5)
    print(f"Connecting to example.com ({ip})|{ip}|:443... connected.")
    time.sleep(0.7)
    print("HTTP request sent, awaiting response... 200 OK")
    time.sleep(0.6)

    total_bytes = size_mb * 1024 * 1024
    print(f"Length: {total_bytes} ({size_mb}M) [application/octet-stream]")
    print(f"Saving to: ‘{file}’\n")

    downloaded = 0
    bar_length = 50
    while downloaded < size_mb:
        step = random.uniform(0.5, 2.5)
        downloaded = min(size_mb, downloaded + step)
        percent = int((downloaded / size_mb) * 100)
        filled = int(bar_length * percent / 100)
        bar = "=" * filled + ">" + " " * (bar_length - filled - 1)

        # speed in MB/s
        speed = random.uniform(0.8, 8.0)
        eta = max(0, (size_mb - downloaded) / speed)

        sys.stdout.write(
            f"\r{file:20} {percent}%[{bar}] {downloaded:.1f}M/{size_mb}M {speed:.1f}MB/s eta {eta:.1f}s"
        )
        sys.stdout.flush()
        time.sleep(random.uniform(0.2, 0.5))

    print("\n\nDownload complete.\n")
    time.sleep(0.6)
    print(f"‘{file}’ saved [{total_bytes}/{total_bytes}]")


def apt_style_progress(package, size_kb=35000):
    print("Reading package lists... Done")
    time.sleep(0.7)
    print("Building dependency tree       ")
    time.sleep(0.6)
    print("Reading state information... Done")
    time.sleep(0.8)

    # Simulate multiple packages (dependencies + extras)
    pkg_list = [
        package,
        f"lib{package}{random.randint(1,9)}",
        f"{package}-common",
        f"{package}-data",
        f"{package}-utils",
        f"libc6",
        f"libgcc-s1",
        f"libstdc++6",
        f"bash",
        f"coreutils",
    ]
    random.shuffle(pkg_list)
    pkg_list = pkg_list[: random.randint(5, 10)]  # pick 5–10 packages

    total_download = 0
    for i, pkg in enumerate(pkg_list, 1):
        size = random.randint(200, 5000)  # each package 200 KB – 5 MB
        total_download += size
        print(
            f"Get:{i} http://archive.ubuntu.com/ubuntu focal/main amd64 {pkg} amd64 "
            f"{random.randint(1,5)}.{random.randint(0,9)} [{size} kB]"
        )
        time.sleep(random.uniform(0.2, 0.8))

    # Simulate total fetched info
    total_time = random.uniform(1.0, 3.5)
    speed = int(total_download / total_time / random.uniform(500, 1500))
    print(f"Fetched {total_download} kB in {total_time:.1f}s ({speed} kB/s)")
    time.sleep(0.8)

    print(f"Selecting previously unselected package {package}.")
    time.sleep(1)
    print(
        f"Preparing to unpack .../{package}_{random.randint(1,5)}.{random.randint(0,9)}_amd64.deb ..."
    )
    time.sleep(0.7)
    print(f"Unpacking {package} ({random.randint(1,5)}.{random.randint(0,9)}) ...")
    time.sleep(1.2)

    print(f"Setting up {package} ({random.randint(1,5)}.{random.randint(0,9)}) ...")
    time.sleep(1.2)

    # Simulate trigger updates
    print("Processing triggers for man-db (2.9.1-1) ...")
    time.sleep(1.0)
    print("Processing triggers for libc-bin (2.31-0ubuntu9.9) ...\n")


def pip_style_progress(package, size_mb=10):
    print(f"Collecting {package}")
    print(
        f"  Downloading {package}-{random.randint(1,5)}.{random.randint(0,9)}.{random.randint(0,9)}.whl ({size_mb} MB)"
    )

    # total download time between 1 to 5 minutes
    total_time = random.randint(60, 300)
    downloaded = 0
    steps = 100  # number of progress updates
    step_size = size_mb / steps
    delay_per_step = total_time / steps

    while downloaded < size_mb:
        downloaded = min(size_mb, downloaded + step_size)
        percent = int((downloaded / size_mb) * 100)
        bar = "━" * int(percent / 2) + " " * (50 - int(percent / 2))
        sys.stdout.write(
            f"\r     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ {downloaded:.1f}/{size_mb} MB {percent}%"
        )
        sys.stdout.flush()
        time.sleep(delay_per_step)

    print(f"\nSuccessfully installed {package}\n")


# ========== Techy Phrases ==========
# ========== Techy Phrases ==========
phrases = [
    # === Mostly INFO/TRACE (white) ===
    (
        Fore.WHITE,
        "[INFO] Loaded configuration file '/etc/sysconfig/network-scripts/ifcfg-eth0' with 17 active parameters.",
    ),
    (
        Fore.WHITE,
        "[TRACE] Established persistent TCP connection to 172.16.44.12:5432 (PostgreSQL cluster node #3).",
    ),
    (
        Fore.WHITE,
        "[INFO] Daemon 'auditd' initialized successfully — monitoring 1,482 system calls.",
    ),
    (
        Fore.WHITE,
        "[DEBUG] Commit log segment rotated: /var/lib/cassandra/commitlog/CommitLog-13-1729476123.log.",
    ),
    (
        Fore.WHITE,
        "[TRACE] Background garbage collector cycle triggered for Java heap region (allocated 2.1GB).",
    ),
    (
        Fore.WHITE,
        "[INFO] Filesystem ext4 mounted on /dev/sdb1 with journal size 128MB and inode table depth 5.",
    ),
    (
        Fore.WHITE,
        "[DEBUG] Thread-pool executor scaled up: 64 active threads, 12 idle, max backlog queue length 8192.",
    ),
    (
        Fore.WHITE,
        "[TRACE] Replication factor set to 3 — synchronizing blocks to secondary node at dc2-storage-14.",
    ),
    (
        Fore.WHITE,
        "[INFO] TLS session resumed with cipher suite ECDHE-RSA-AES256-GCM-SHA384 after 0.423s handshake.",
    ),
    (
        Fore.WHITE,
        "[TRACE] Kafka consumer group 'analytics_pipeline' rebalanced — partition #12 assigned to node-7.",
    ),
    (
        Fore.WHITE,
        "[DEBUG] Kernel perf counters: 2,139,444 context switches recorded in the last 60 seconds.",
    ),
    (
        Fore.WHITE,
        "[TRACE] Executed SQL migration V2025_09_10_03__add_index_user_last_login.sql (took 412ms).",
    ),
    (
        Fore.WHITE,
        "[INFO] Systemd unit 'docker.service' entered 'active (running)' state at 01:23:41 UTC.",
    ),
    (
        Fore.WHITE,
        "[DEBUG] Page cache flush completed: 823MB written to /dev/sda at 112 MB/s throughput.",
    ),
    (
        Fore.WHITE,
        "[TRACE] RPC call executed: service=UserDirectory method=GetUserPermissions duration=742ms.",
    ),
    (
        Fore.WHITE,
        "[INFO] Remote backup uploaded to S3 bucket 'infra-snapshots' (checksum verified: sha256=afe9321b...).",
    ),
    (
        Fore.WHITE,
        "[DEBUG] Swap usage normalized — 1.8GB freed by offloading inactive pages to zswap compressed cache.",
    ),
    (
        Fore.WHITE,
        "[TRACE] Audit record: uid=0 action=CAP_NET_ADMIN requested by pid=1123 (/usr/bin/ip link set).",
    ),
    (
        Fore.WHITE,
        "[INFO] Transaction batch committed: 38,492 inserts, 4,882 updates, 0 conflicts, duration=2.93s.",
    ),
    (
        Fore.WHITE,
        "[DEBUG] Container runtime pulled image registry.company.com/core/api-service:build-44192 in 4.3s.",
    ),
    # === Warnings (yellow, random/longer) ===
    (
        Fore.YELLOW,
        "WARNING: Detected high I/O latency on block device /dev/nvme0n1 — average read 392ms (threshold 50ms).",
    ),
    (
        Fore.YELLOW,
        "WARNING: DNS resolver 'systemd-resolved' reported 27 consecutive query timeouts to upstream 8.8.8.8.",
    ),
    (
        Fore.YELLOW,
        "WARNING: JVM heap occupancy exceeds 89% — GC pressure increasing, potential allocation stalls expected.",
    ),
    (
        Fore.YELLOW,
        "WARNING: Network congestion on interface eth0 — packet loss measured at 14.2% over 60s interval.",
    ),
    (
        Fore.YELLOW,
        "WARNING: Filesystem journal replay required for /dev/sdc1 — previous shutdown marked as unclean.",
    ),
    (
        Fore.YELLOW,
        "WARNING: Node clock drift detected (offset +2m43s) — synchronizing with NTP peer 192.168.2.1.",
    ),
    (
        Fore.YELLOW,
        "WARNING: TLS renegotiation requested by client but not permitted — session may terminate unexpectedly.",
    ),
    (
        Fore.YELLOW,
        "WARNING: Service 'nginx' worker process 28374 consuming excessive memory (RSS: 1.9GB).",
    ),
    (
        Fore.YELLOW,
        "WARNING: Queue backlog exceeded safe threshold (17,291 pending messages). Delivery latency rising.",
    ),
    (
        Fore.YELLOW,
        "WARNING: Deprecated configuration key 'net.ipv4.tcp_tw_reuse' found in sysctl.conf (ignored).",
    ),
    # === Critical/Errors (red) ===
    (
        Fore.RED,
        "CRITICAL: InnoDB storage engine crashed — corruption detected in redo log sequence #29294818.",
    ),
    (
        Fore.RED,
        "ERROR: Failed to attach shared memory segment 0x7f99de920000 (EINVAL) — possible ABI mismatch.",
    ),
    (
        Fore.RED,
        "FATAL: Process 1092 (java) received signal SIGBUS while accessing address 0x00007f2214aa0000.",
    ),
    (
        Fore.RED,
        "PANIC: Primary etcd cluster member lost quorum — majority of nodes unreachable.",
    ),
    (
        Fore.RED,
        "CRITICAL: Kernel BUG at mm/memory.c:1881! #PF: supervisor read access in kernel mode.",
    ),
    (
        Fore.RED,
        "FATAL: RAID controller firmware timeout on channel 2 — drive array degraded.",
    ),
    (
        Fore.RED,
        "CRITICAL: OOM killer invoked — terminated process 8821 (postgres) using 4.3G memory.",
    ),
    (
        Fore.RED,
        "ERROR: GPU device /dev/nvidia0 reported ECC errors (23 corrected, 4 uncorrected) in last 120s.",
    ),
    (
        Fore.RED,
        "FATAL: System integrity violation — signed kernel module replaced by unsigned variant.",
    ),
    (
        Fore.RED,
        "CRITICAL: Journal replay aborted — metadata corruption detected on /dev/mapper/vg0-lv_home.",
    ),
    # === More White / filler realistic noise ===
    (
        Fore.WHITE,
        "[DEBUG] Journal flushed: 14,288 log entries written to disk (batch id=2025-09-11T00:15:33Z).",
    ),
    (
        Fore.WHITE,
        "[INFO] Secure shell session established from 10.14.33.92 using ed25519 key fingerprint SHA256:vBn...",
    ),
    (
        Fore.WHITE,
        "[TRACE] Service mesh envoy proxy reloaded config with 19 new cluster endpoints.",
    ),
    (
        Fore.WHITE,
        "[INFO] Rebalanced shard group #14 across 3 nodes due to uneven key distribution.",
    ),
    (
        Fore.WHITE,
        "[DEBUG] Temporary file cleanup removed 982 orphaned files from /tmp (freed 438MB).",
    ),
    (
        Fore.WHITE,
        "[INFO] CRON job 'backup-daily' executed at 02:00:00 — result=success duration=183.2s.",
    ),
    (
        Fore.WHITE,
        "[TRACE] SSL certificate chain validation completed — 3 intermediates, root=ISRG Root X1.",
    ),
    (
        Fore.WHITE,
        "[DEBUG] Prometheus scrape cycle completed: 423 targets queried in 6.38s.",
    ),
    (
        Fore.WHITE,
        "[INFO] Policy engine evaluated 892 rules, 0 violations, execution time=113ms.",
    ),
    (
        Fore.WHITE,
        "[TRACE] Docker overlay network created with ID 72c84c1d92a (subnet 10.42.0.0/16).",
    ),
    # === Sprinkle more long scary reds ===
    (
        Fore.RED,
        "CRITICAL: Filesystem consistency check failed — orphaned inode list contains 13,728 entries.",
    ),
    (
        Fore.RED,
        "PANIC: Fatal double fault occurred in ring 0 — CPU halted at 0xffffffff8100ae92.",
    ),
    (
        Fore.RED,
        "ERROR: Checkpoint/restore operation failed: missing memory map segment for pid=22101.",
    ),
    (
        Fore.RED,
        "FATAL: Distributed transaction rollback failed — 1 participant left in 'prepared' state.",
    ),
    (
        Fore.RED,
        "CRITICAL: Init process (pid=1) terminated unexpectedly — system requires manual intervention.",
    ),
    (
        Fore.RED,
        "PANIC: Hardware watchdog detected system lockup (>120s) — triggering forced reboot.",
    ),
]

# ========== Fake Packages ==========
packages = [
    # Python libraries (real ones)
    "numpy",
    "pandas",
    "matplotlib",
    "scipy",
    "scikit-learn",
    "tensorflow",
    "torch",
    "keras",
    "flask",
    "django",
    "fastapi",
    "sqlalchemy",
    "requests",
    "httpx",
    "urllib3",
    "opencv-python",
    "pillow",
    "lxml",
    "beautifulsoup4",
    "scrapy",
    "pytest",
    "unittest2",
    "nose2",
    "hypothesis",
    "coverage",
    "sphinx",
    "mkdocs",
    "pyyaml",
    "jinja2",
    "markupsafe",
    "black",
    "flake8",
    "pylint",
    "mypy",
    "isort",
    "cryptography",
    "pyopenssl",
    "paramiko",
    "bcrypt",
    "passlib",
    "pydantic",
    "dataclasses-json",
    "attrs",
    "marshmallow",
    "typer",
    "click",
    "rich",
    "textual",
    "prompt_toolkit",
    "colorama",
    "fasttext",
    "nltk",
    "spacy",
    "transformers",
    "sentencepiece",
    "pyarrow",
    "dask",
    "polars",
    "vaex",
    "modin",
    "sqlparse",
    "mysqlclient",
    "psycopg2",
    "pymongo",
    "redis",
    "celery",
    "rq",
    "kombu",
    "aioredis",
    "asyncpg",
    "aiohttp",
    "trio",
    "curio",
    "websockets",
    "uvloop",
    "pyqt5",
    "pyside6",
    "tkinter",
    "kivy",
    "wxpython",
    "pyinstaller",
    "cx_Freeze",
    "nuitka",
    "cffi",
    "cython",
    "numba",
    "joblib",
    "multiprocess",
    "ray",
    "dill",
    "seaborn",
    "plotly",
    "bokeh",
    "altair",
    "holoviews",
    "statsmodels",
    "sympy",
    "theano",
    "jax",
    "h5py",
    # System-style / hackerish
    "libcrypto-1.2.0",
    "kernel-patch-x86_64",
    "python-dev-tools",
    "ai-core-module",
    "darknet-driver",
    "websocket-libc",
    "quantum-tunnel-bridge",
    "neural-net-enhancer",
    "syslog-daemon",
    "nmap-utils",
    "deepfake-generator",
    "fusion-core",
    "libssl-legacy",
    "matrix-simulator",
    "cyberpunk-protocol",
    "dns-over-tor",
    "rootkit-sanitizer",
    "wormhole-proxy",
    "stealth-injector",
    "malnet-scanner",
    "glitchware-patch",
    "bios-updater-x99",
    "sandbox-escaper",
    "tor-relay-client",
    "quantum-key-distributor",
    "entropy-mixer",
    "memory-fragmenter",
    "ghost-tracker",
    "vm-escape-module",
    "kernel-shield",
    "hypervisor-hook",
    "stacktrace-analyzer",
    "exploit-db-sync",
    "payload-dropper",
    "obfuscator-engine",
    "crypto-wallet-daemon",
]

# ========== Installer Tasks ==========
installer_tasks = [
    "Installing core components",
    "Updating system libraries",
    "Deploying security patches",
    "Building kernel modules",
    "Configuring runtime environment",
    "Optimizing memory manager",
]


def fake_package_install():
    package = random.choice(packages)
    print(Fore.MAGENTA + f"\n[INSTALLER] Installing package: {package}...\n")
    random_progress(f"Downloading {package}", package=package)
    random_progress(f"Extracting {package}", package=package)
    random_progress(f"Configuring {package}", package=package)

    print(Fore.GREEN + f"[SUCCESS] Package {package} installed successfully.\n")


def installer_sequence():
    print(Fore.MAGENTA + "\n[INSTALLER] Installation sequence triggered...\n")
    task = random.choice(installer_tasks)
    progress_bar(task, duration=random.randint(10, 25))


# ========== Chaotic Extras ==========
def fake_bsod():
    print(Fore.WHITE + Style.BRIGHT + "\n\n=== SYSTEM FAILURE ===")
    print(Fore.BLUE + Style.BRIGHT + "STOP CODE: CRITICAL_PROCESS_DIED")
    print("Collecting crash dump... [34%]")
    time.sleep(4)
    print("System will reboot automatically.\n")


def glitch_text():
    glitch = "".join(random.choice("█▒▓░#@!%$&*?<>") for _ in range(40))
    print(Fore.MAGENTA + "[GLITCH] " + glitch)


def fake_prompt():
    print(Fore.CYAN + "Enter encryption key to continue: ", end="")
    time.sleep(2)
    print(Fore.GREEN + " ******** [OK]")


def fake_reboot():
    print(Fore.YELLOW + "\n[REBOOT] Restarting system services...\n")
    time.sleep(5)
    print(Fore.GREEN + "[RECOVERY] Filesystem mounted in safe mode.\n")


def fake_hex_dump():
    dump = " ".join(hex(random.randint(0, 255)) for _ in range(16))
    print(Fore.CYAN + f"[DUMP] {dump}")


def self_destruct():
    print(Fore.RED + "\n[WARNING] Self-destruct sequence initiated... T-30s")
    for i in range(30, 0, -5):
        print(Fore.RED + f"T-{i} seconds...")
        time.sleep(1)
    print(Fore.GREEN + "[CANCELLED] Abort command received.\n")


def easter_egg():
    print(Fore.GREEN + "[EASTER_EGG] Running DOOM... (just kidding)\n")


# ========== Endless Scroll ==========
def endless_scroll():
    try:
        while True:
            roll = random.random()

            # Installer events
            if roll > 0.85:
                installer_sequence()
            elif roll > 0.75:
                fake_package_install()
            else:
                color, line = random.choice(phrases)

                # Random noise
                if random.random() > 0.6:
                    line += f" [{random.randint(0,100)}%]"
                if random.random() > 0.7:
                    line += f" (code: 0x{random.randint(1000,99999):X})"

                print(color + line)

            # Random chaotic events
            chaos = random.random()
            if chaos > 0.999:
                fake_bsod()
            elif chaos > 0.998:
                glitch_text()
            elif chaos > 0.997:
                fake_prompt()
            elif chaos > 0.996:
                fake_reboot()
            elif chaos > 0.995:
                fake_hex_dump()
            elif chaos > 0.994:
                self_destruct()
            elif chaos > 0.993:
                easter_egg()

            # Random pauses
            time.sleep(random.uniform(0.3, 1.0))

            if random.random() > 0.99:
                print(
                    Fore.CYAN
                    + "\n[PAUSE] System checkpoint reached. Verifying integrity...\n"
                )
                time.sleep(3)

            if random.random() > 0.995:
                print(
                    Fore.RED
                    + "\n[FREEZE] Critical process unresponsive... waiting...\n"
                )
                time.sleep(random.uniform(5, 7))

    except KeyboardInterrupt:
        print(Fore.YELLOW + "\n[Process Terminated by User]")


# ========== Main ==========
if __name__ == "__main__":
    print(Fore.CYAN + "Initializing system logs...\n")
    endless_scroll()
