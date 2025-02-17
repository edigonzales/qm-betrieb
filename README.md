# qm-betrieb

```
conda create -n qm-betrieb python=3.12
```

```
conda activate qm-betrieb
```

```
conda remove --name qm-betrieb --all
```

```
pip install -r requirements.txt
```

```
{
  "default-service-strategy": "deny",
  "services": {
    "sos": {
      "type": "allow"
    }
  }
}
```

Für feingranulierteres IAM (z.B. read-only für eine Policy) muss das CLI verwendet werden: https://chatgpt.com/c/67b2f2d0-3a28-8008-a581-a0dbd37d34de

