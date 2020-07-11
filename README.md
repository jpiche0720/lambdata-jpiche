# lambdata-jpiche
Python Package 

## Installation
```
pip install -i https://test.pypi.org/simple/ joshuatree==1.3
```
## Usage

### Pobabililty of true given a positive test result
```
p_true_prior = 1/1000
false_positive_rate= 5/100
true_positive_rate = 1

prob_true_given_positive(p_true_prior, false_positive_rate,true_positive_rate)

```
### Insert Row into a dataframe
```
data = {'A':[2,2,3,3,4], 'B':[1,2,4,6,7], 'C': [2,3,5,7,8]}
df = pd.DataFrame(data)
print(df)

df = insert_row(df, 2, ['ADD','ADD','ADD'])
print(df)

```
### Serial Communication Class
```
hardware = Brain('interial','range finder','pi','ad')
print(hardware.imu,'and', hardware.range_find)
hardware.calculate()
```


