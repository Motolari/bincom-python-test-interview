CREATE TABLE IF NOT EXISTS public.colour_freq (
    colour VARCHAR(20) PRIMARY KEY,
    frequency INT
);


INSERT INTO public.colour_freq (colour, frequency) VALUES ('GREEN', 10) ON CONFLICT (colour) DO UPDATE SET frequency = EXCLUDED.frequency;
INSERT INTO public.colour_freq (colour, frequency) VALUES ('YELLOW', 5) ON CONFLICT (colour) DO UPDATE SET frequency = EXCLUDED.frequency;
INSERT INTO public.colour_freq (colour, frequency) VALUES ('BROWN', 6) ON CONFLICT (colour) DO UPDATE SET frequency = EXCLUDED.frequency;
INSERT INTO public.colour_freq (colour, frequency) VALUES ('BLUE', 31) ON CONFLICT (colour) DO UPDATE SET frequency = EXCLUDED.frequency;
INSERT INTO public.colour_freq (colour, frequency) VALUES ('PINK', 5) ON CONFLICT (colour) DO UPDATE SET frequency = EXCLUDED.frequency;
INSERT INTO public.colour_freq (colour, frequency) VALUES ('ORANGE', 9) ON CONFLICT (colour) DO UPDATE SET frequency = EXCLUDED.frequency;
INSERT INTO public.colour_freq (colour, frequency) VALUES ('CREAM', 2) ON CONFLICT (colour) DO UPDATE SET frequency = EXCLUDED.frequency;
INSERT INTO public.colour_freq (colour, frequency) VALUES ('RED', 9) ON CONFLICT (colour) DO UPDATE SET frequency = EXCLUDED.frequency;
INSERT INTO public.colour_freq (colour, frequency) VALUES ('WHITE', 16) ON CONFLICT (colour) DO UPDATE SET frequency = EXCLUDED.frequency;
INSERT INTO public.colour_freq (colour, frequency) VALUES ('ASH', 1) ON CONFLICT (colour) DO UPDATE SET frequency = EXCLUDED.frequency;
INSERT INTO public.colour_freq (colour, frequency) VALUES ('BLACK', 1) ON CONFLICT (colour) DO UPDATE SET frequency = EXCLUDED.frequency;