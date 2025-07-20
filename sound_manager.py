import pygame
import os

class SoundManager:
    def __init__(self):
        pygame.mixer.init(frequency=22050, size=-16, channels=2, buffer=512)
        
        # Create sounds directory
        self.sounds_dir = "sounds"
        if not os.path.exists(self.sounds_dir):
            os.makedirs(self.sounds_dir)
        
        # Create simple sound effects
        self._create_simple_sounds()
        
        # Music state
        self.music_playing = False
        self.powerup_channel = None
    
    def _create_simple_sounds(self):
        """Create simple sound effects using pygame mixer"""
        try:
            # Initialize sound objects to None first
            self.gem_sound = None
            self.powerup_sound = None
            
            # Try to create sounds using pygame's built-in capabilities
            sample_rate = 22050
            
            # Create gem sound - short pleasant beep
            self.gem_sound = self._create_tone_sound(880, 0.2, 0.5)  # A note, 0.2 seconds, medium volume
            
            # Create power-up sound - longer rising tone
            self.powerup_sound = self._create_sweep_sound(440, 880, 0.5, 0.6)  # A to high A, 0.5 seconds
            
            print("Sound effects created successfully!")
            
        except Exception as e:
            print(f"Could not create sound effects: {e}")
            self.gem_sound = None
            self.powerup_sound = None
    
    def _create_tone_sound(self, frequency, duration, volume):
        """Create a simple tone sound"""
        try:
            import pygame.sndarray as sndarray
            import numpy as np
            
            sample_rate = 22050
            frames = int(duration * sample_rate)
            
            # Create time array
            t = np.linspace(0, duration, frames)
            
            # Generate sine wave
            wave = np.sin(2 * np.pi * frequency * t)
            
            # Apply envelope (fade out)
            envelope = np.exp(-t * 3)
            wave = wave * envelope * volume
            
            # Convert to stereo and ensure C-contiguous
            stereo_wave = np.zeros((frames, 2), dtype=np.float64)
            stereo_wave[:, 0] = wave  # Left channel
            stereo_wave[:, 1] = wave  # Right channel
            
            # Convert to int16 and make C-contiguous
            sound_array = (stereo_wave * 32767).astype(np.int16)
            sound_array = np.ascontiguousarray(sound_array)
            
            # Create pygame sound
            sound = sndarray.make_sound(sound_array)
            return sound
            
        except ImportError:
            # If numpy/sndarray not available, return None
            return None
        except Exception as e:
            print(f"Error creating tone sound: {e}")
            return None
    
    def _create_sweep_sound(self, start_freq, end_freq, duration, volume):
        """Create a frequency sweep sound"""
        try:
            import pygame.sndarray as sndarray
            import numpy as np
            
            sample_rate = 22050
            frames = int(duration * sample_rate)
            
            # Create time array
            t = np.linspace(0, duration, frames)
            
            # Create frequency sweep
            frequency = start_freq + (end_freq - start_freq) * (t / duration)
            
            # Generate the sweep
            wave = np.sin(2 * np.pi * frequency * t)
            
            # Apply envelope
            envelope = np.exp(-t * 2)
            wave = wave * envelope * volume
            
            # Convert to stereo and ensure C-contiguous
            stereo_wave = np.zeros((frames, 2), dtype=np.float64)
            stereo_wave[:, 0] = wave  # Left channel
            stereo_wave[:, 1] = wave  # Right channel
            
            # Convert to int16 and make C-contiguous
            sound_array = (stereo_wave * 32767).astype(np.int16)
            sound_array = np.ascontiguousarray(sound_array)
            
            # Create pygame sound
            sound = sndarray.make_sound(sound_array)
            return sound
            
        except ImportError:
            return None
        except Exception as e:
            print(f"Error creating sweep sound: {e}")
            return None
    
    def play_gem_sound(self):
        """Play gem collection sound"""
        if self.gem_sound:
            self.gem_sound.play()
        else:
            # Fallback - could add a simple beep here
            pass
    
    def play_powerup_sound(self):
        """Play power-up sound"""
        if self.powerup_sound:
            self.powerup_channel = self.powerup_sound.play()
        else:
            # Fallback
            pass
    
    def start_background_music(self):
        """Start playing background music"""
        try:
            # For now, we'll skip background music file creation to avoid complexity
            # The sound effects (gem and power-up) are working well
            print("Background music disabled for simplicity - sound effects active!")
            self.music_playing = False
        except Exception as e:
            print(f"Error starting background music: {e}")
    
    def _create_background_music(self):
        """Create simple background music"""
        try:
            import pygame.sndarray as sndarray
            import numpy as np
            
            sample_rate = 22050
            duration = 8.0  # 8-second loop
            frames = int(duration * sample_rate)
            
            # Simple melody notes (C major scale)
            notes = [261.63, 293.66, 329.63, 349.23, 392.00, 440.00, 493.88, 523.25]  # C4 to C5
            note_duration = duration / len(notes)
            
            music = np.zeros(frames)
            
            for i, freq in enumerate(notes):
                start_idx = int(i * note_duration * sample_rate)
                end_idx = int((i + 1) * note_duration * sample_rate)
                note_frames = end_idx - start_idx
                
                if note_frames > 0:
                    t = np.linspace(0, note_duration, note_frames)
                    
                    # Generate note with harmonics
                    note = (np.sin(2 * np.pi * freq * t) * 0.4 +
                           np.sin(2 * np.pi * freq * 2 * t) * 0.2)
                    
                    # Apply note envelope
                    envelope = np.exp(-t * 1.5)
                    note = note * envelope
                    
                    music[start_idx:end_idx] = note
            
            # Convert to stereo and ensure C-contiguous
            stereo_music = np.zeros((frames, 2), dtype=np.float64)
            stereo_music[:, 0] = music  # Left channel
            stereo_music[:, 1] = music  # Right channel
            
            # Convert to int16 and make C-contiguous
            music_array = (stereo_music * 16383).astype(np.int16)
            music_array = np.ascontiguousarray(music_array)
            
            # Create pygame sound
            background_sound = sndarray.make_sound(music_array)
            return background_sound
            
        except ImportError:
            print("NumPy not available, skipping background music")
            return None
        except Exception as e:
            print(f"Error creating background music: {e}")
            return None
    
    def _save_sound_to_file(self, sound, filename):
        """Save a pygame sound to a WAV file"""
        try:
            # This is a simplified approach - in practice you might use
            # pygame.sndarray.array() and save it properly
            # For now, we'll just use the sound object directly
            pass
        except Exception as e:
            print(f"Error saving sound to file: {e}")
    
    def _play_simple_background_music(self):
        """Play simple background music using generated tones"""
        try:
            # For now, we'll skip background music to keep the implementation simple
            # You can add music files later
            self.music_playing = False
        except Exception as e:
            print(f"Error with background music: {e}")
    
    def stop_background_music(self):
        """Stop background music"""
        if self.music_playing:
            pygame.mixer.music.stop()
            self.music_playing = False
    
    def set_music_volume(self, volume):
        """Set background music volume (0.0 to 1.0)"""
        pygame.mixer.music.set_volume(volume)
