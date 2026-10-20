from pathlib import Path
import numpy as np,soundfile as sf
p=Path(__file__).resolve().parents[1];sr=24000;t=np.arange(sr*25)/sr
# Original, understated harmonic pad; no third-party music recordings.
fade=np.minimum(t/2,1)*np.minimum((25-t)/1.3,1)
a=sum(.0023*np.sin(2*np.pi*f*t+.18*np.sin(2*np.pi*.07*t)) for f in [130.8128,196,261.6256,329.6276])*fade
for pos in [.3,15.1]:
    u=np.maximum(0,t-pos);env=(t>=pos)*np.exp(-u*3.2)
    a+=.009*np.sin(2*np.pi*1046.5*u)*env
sf.write(p/'assets/ambience.wav',a.astype(np.float32),sr)
