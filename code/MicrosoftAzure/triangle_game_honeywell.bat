@set version=2

@FOR /L %%A IN (0,1,11) DO az quantum job submit --target-id honeywell.hqs-lt-1.0 --shots 1000 --job-name move%%A.%version% -- --index=%%A > out/move%%A.%version% &



