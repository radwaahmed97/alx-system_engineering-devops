# Install an version of flask (2.1.0)
package {'flask':
  ensure   => '2.1.0',
  provider => 'pip3'
}

package {'werkseug':
  ensure   => '2.1.1',
  provider => 'pip3',
}
