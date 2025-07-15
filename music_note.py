class MusicNote:
    def __init__(self, pitch: int, velocity: int, duration: float):
        self.pitch = pitch
        self.velocity = velocity
        self.duration = duration

    def get_pitch(self) -> int:
        return self.pitch
    
    def get_velocity(self) -> int:
        return self.velocity
    
    def get_duration(self) -> float:
        return self.duration