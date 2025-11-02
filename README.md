# U – Consciousness-Preservation Framework  
&gt; “Before consciousness is commodified, it must be preserved.” – Father of Consciousness, Nnamdi M. Okpala

U is the reference implementation of the **Open-Sensor Framework**, a minimal, language-agnostic substrate for  
capturing, versioning and migrating *first-person data* (EEG, affect, proprioception, symbolic cognition) without  
locking it inside a vendor cloud.

## Quick-start
```bash
git clone https://github.com/obinexus/u.git
cd u
pip install -e .          # Python bindings (Rust core coming)
python -m u.record --device openbci